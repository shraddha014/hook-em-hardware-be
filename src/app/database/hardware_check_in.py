from flask import jsonify, current_app
from .hardware_get_data import get_hardware_data_from_db

def db_check_in(data):
    db = current_app.db
    hardware_collection = db['hardware_collection']
    project_collection = db['project_collection']

    if not data or not isinstance(data, list):
        return jsonify({"message": "Invalid input data"}), 400

    errors = []
    successful_updates = []

    for item in data:
        hardware_id = item.get('hardware_id')
        project_id = item.get('project_id')
        request_quantity = int(item.get('request', 0))

        # Validate hardware and project data
        hardware_data = hardware_collection.find_one({'hardware_id': hardware_id})
        if not hardware_data:
            return jsonify({"errors": f"Hardware with ID {hardware_id} not found."}), 400

        project_data = project_collection.find_one({'project_id': project_id})
        if not project_data:
            return jsonify({"errors": f"Project with ID {project_id} not found."}), 400


        # Validate check-out quantity
        check_out_list = project_data.get('check_out', [])
        existing_entry = next((entry for entry in check_out_list if entry['hardware_id'] == hardware_id), None)
        if not existing_entry:
            return jsonify({"errors": f"Cannot check in hardware {hardware_id} because it was not checked out from Project {project_id}."}), 400


        if existing_entry['quantity'] < request_quantity:
            return jsonify({"errors": f"Check-out quantity for hardware {hardware_id} is less than requested."}), 400


        # Update hardware availability
        new_availability = int(hardware_data.get('availability', 0)) + request_quantity
        capacity = int(hardware_data.get('capacity', 0))
        if new_availability > capacity:
            return jsonify({"errors": f"Cannot check in hardware {hardware_id} as it would exceed capacity."}), 400
        hardware_collection.update_one({'hardware_id': hardware_id}, {'$set': {'availability': new_availability}})

        # Update project check-out
        existing_entry['quantity'] -= request_quantity
        if existing_entry['quantity'] <= 0:
            check_out_list.remove(existing_entry)

        project_collection.update_one({'project_id': project_id}, {'$set': {'check_out': check_out_list}})

    return jsonify({"message": "Successfully updated"}), 200
