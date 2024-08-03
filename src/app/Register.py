
from flask import jsonify, current_app
from pymongo import MongoClient


def add_user(request):
    data = request.get_json()
    db = current_app.db
    
    # Get user data from the JSON payload
    name = data.get('username')
    email = data.get('email')
    password = data.get('password')

    #check for existing users, save to the database)
    if not name or not email or not password:
        return jsonify({"message": "Missing required fields"}), 400
    
    existing_user = db['user_collection'].find_one({"$or": [{"username": name}, {"email": email}]})
    if existing_user:
        if existing_user['username'] == name:
            return jsonify({"message": "Username already exists"}), 400
        if existing_user['email'] == email:
            return jsonify({"message": "Email already exists"}), 400  
    db['user_collection'].insert_one(data)  
    # save the user data to a database
    return jsonify({"message": "User registered successfully"}), 200