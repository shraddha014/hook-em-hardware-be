from flask import jsonify, current_app
from bson import ObjectId

def convert_object_id(document):
    """Convert ObjectId fields to string in a MongoDB document."""
    if isinstance(document, list):
        return [convert_object_id(doc) for doc in document]
    if isinstance(document, dict):
        return {k: (str(v) if isinstance(v, ObjectId) else convert_object_id(v)) for k, v in document.items()}
    return document

def get_user_associated_project_id(user_name):
    db = current_app.db
    collection = db['user_collection']
    project_collection= db['project_collection']
    documents = collection.find_one({"username": user_name})  # Find all documents, exclude _id
    if documents:
        project_ids = documents.get('projects_list', [])
        projects = []
        for project_id in project_ids:
            project = project_collection.find_one({"project_id": (project_id)})
            if project:
                projects.append(convert_object_id(project))
        return jsonify(projects), 200
    return jsonify({"message": "you have no projects"}), 400

def get_project_from_project_id(project_id):
    db = current_app.db
    collection = db['project_collection']
    documents = collection.find({"project_id": project_id})  # Find all documents, exclude _id
    documents = convert_object_id(documents)
    if documents:
        return jsonify((documents)), 200
    return jsonify({"message": "There is no project associated with the id"}), 400

def set_project_list_user(data):
    db = current_app.db
    user_collection = db['user_collection']

    # Find the user document
    user_doc = user_collection.find_one({'username': data['username']})

    if user_doc:
        # Append the project_id to the projects_list
        projects = user_doc.get('projects_list', [])
        projects.append(data['project_id'])

        # Update the user document with the new projects_list
        user_collection.update_one(
            {'username': data['username']},
            {'$set': {'projects_list': projects}}
        )
        return {'status': 'success', 'message': 'Project list updated'}
    else:
        # Handle the case where the user document does not exist
        return {'status': 'error', 'message': 'User not found'}



