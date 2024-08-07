from flask import jsonify, current_app
from .project_list import set_project_list_user

def create_project(name, user_name, description, project_id):
    db = current_app.db
    user_collection = db['user_collection']
    project_collection = db['project_collection']
    
    # Retrieve user_id by user_name
    user_doc = user_collection.find_one({"username": user_name})
    if not user_doc:
        return {'message': 'Error: User not found'}, 404

    project_doc = project_collection.find_one({"project_id": project_id})
    print("project_doc", project_doc)
    if project_doc:
        # Check if a project with the same project_id already exists
        return {'message': 'Error: Project with this ID already exists'}, 409 
    else:
        # If no existing project is found, proceed to create a new one
        new_project = {"name": name, "description": description, "project_id": project_id}
        result = project_collection.insert_one(new_project)
        if result.acknowledged:
            #add project_id into the user
            set_project_list_user({'username': user_name, 'project_id': project_id})
            return {'message': 'Project created successfully!', 'project_id': str(result.inserted_id)}, 201
        else:
            return {'message': 'Error creating project'}, 500 
    