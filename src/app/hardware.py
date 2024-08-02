

from flask import jsonify, current_app

def set_hardware_data(data):
    # Use current_app to access the db
    db = current_app.db

    print(db['hardware_collection'])
   
    collection = db['hardware_collection']
    result = collection.insert_one(data)
    if result:
        return jsonify({"message": "Document inserted", "id": str(result.inserted_id)}), 201
    return jsonify({"message": "Invalid input"}), 400

def get_hardware_data():
    db = current_app.db
    collection = db['hardware_collection']
    documents = list(collection.find({}, {"_id": 0}))  # Find all documents, exclude _id
    if documents:
        return jsonify(documents), 200
    return jsonify({"message": "Collection name required"}), 400

