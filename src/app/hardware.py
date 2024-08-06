from flask import jsonify, current_app
from .database.hardware_get_data import get_hardware_data_from_db
from .database.hardware_check_in import db_check_in
from .database.hardware_check_out import db_check_out

def set_hardware_data(data):
    db = current_app.db
    collection = db['hardware_collection']
    result = collection.insert_one(data)
    if result:
        return jsonify({"message": "Document inserted", "id": str(result.inserted_id)}), 201
    return jsonify({"message": "Invalid input"}), 400

def get_hardware_data():
    return get_hardware_data_from_db()


def check_out(request):
    return db_check_out(request)

def check_in(request):
    return db_check_in(request)
