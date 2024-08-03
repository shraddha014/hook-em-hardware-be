from flask import jsonify, current_app
from bson import ObjectId

def convert_object_id(document):
    """Convert ObjectId fields to string in a MongoDB document."""
    if isinstance(document, list):
        return [convert_object_id(doc) for doc in document]
    if isinstance(document, dict):
        return {k: (str(v) if isinstance(v, ObjectId) else convert_object_id(v)) for k, v in document.items()}
    return document


def get_hardware_data_from_db():
    db = current_app.db
    collection = db['hardware_collection']
    
    # Fetch all documents
    documents = list(collection.find({}))
    
    # Convert ObjectId to string
    documents = convert_object_id(documents)
    
    if documents:
        return jsonify(documents), 200
    return jsonify({"message": "No hardware data found"}), 404
