from flask import jsonify, current_app

def create_project(name, user_name, description, project_id):
    db = current_app.db
    user_collection = db['user_collection']
    project_collection = db['project_collection']
    
    # Retrieve user_id by user_name
    user_doc = user_collection.find_one({"username": user_name})
    if not user_doc:
        return {'message': 'Error: User not found'}, 404
    else:
        user_id = user_doc['_id']  # Retrieve the user_id from MongoDB user_collection

    if project_collection.find_one({"project_id": project_id}):
        # Check if a project with the same project_id already exists
        return {'message': 'Error: Project with this ID already exists'}, 409 
    else:
        # If no existing project is found, proceed to create a new one
        new_project = {"name": name, "description": description, "project_id": project_id, "user_id": user_id}
        result = project_collection.insert_one(new_project)
        if result.acknowledged:
            return {'message': 'Project created successfully!', 'project_id': str(result.inserted_id)}, 201
        else:
            return {'message': 'Error creating project'}, 500 
