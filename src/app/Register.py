from flask import jsonify, current_app

def add_user(request):
    data = request.get_json()
    db = current_app.db

    # Get user data from the JSON payload
    name = data.get('username')
    email = data.get('email')
    password = data.get('password')

    # Check for missing fields
    if not name or not email or not password:
        return jsonify({"message": "Missing required fields"}), 400

    # Check for existing username
    existing_username = db['user_collection'].find_one({"username": name})
    if existing_username:
        return jsonify({"message": "Username already exists"}), 400

    # Check for existing email
    existing_email = db['user_collection'].find_one({"email": email})
    if existing_email:
        return jsonify({"message": "Email already exists"}), 400

    # Save the user data to the database
    db['user_collection'].insert_one(data)

    return jsonify({"message": "User registered successfully"}), 200
