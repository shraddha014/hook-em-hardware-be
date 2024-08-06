from flask import jsonify, current_app

def create_project(name, description, project_id):
    db = current_app.db
    project_collection = db['project_collection']
    new_project = {"name": name, "description": description, "project_id": project_id}
    result = project_collection.insert_one(new_project)
    if result.acknowledged:
        return {'message': 'Project created successfully!', 'project_id': str(result.inserted_id)}
    else:
        return {'message': 'Error creating project'}
