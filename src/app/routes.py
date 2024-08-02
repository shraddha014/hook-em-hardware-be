# app/routes.py
from flask import Blueprint, request, jsonify
from flask_cors import CORS
from .hardware import set_hardware_data, get_hardware_data
from .login import login

main_routes = Blueprint('main_routes', __name__)
CORS(main_routes)

@main_routes.route('/set-hardware', methods=["POST"])
def set_hardware():
    data = request.get_json()
    return set_hardware_data(data)

@main_routes.route('/get-hardware', methods=["GET"])
def get_hardware():
    return get_hardware_data()

@main_routes.route('/login', methods=['POST'])
def login_route():
    data = request.get_json()
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