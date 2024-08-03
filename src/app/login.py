from flask import jsonify

def login(data):
    email = data.get('email')
    password = data.get('password')
    
    if not email or not password:
        return jsonify({"error": "Missing email or password"}), 400
    
    user_info = login(email, password)
    if user_info:
        return jsonify({
            "message": "Login successful",
            "username": user_info['username']
        }), 200
    else:
        return jsonify({"error": "Invalid email or password"}), 401