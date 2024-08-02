from flask import current_app, jsonify

def login(email, password):
    db = current_app.db
    user_collection = db['user_collection']
    
    user = user_collection.find_one({'email': email, 'password': password})
    if user:
        return {'username': user.get('username')}
    return None