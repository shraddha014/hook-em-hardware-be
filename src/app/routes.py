# app/routes.py
from flask import Blueprint, request, jsonify
from flask_cors import CORS
from .login import login
from .hardware import set_hardware_data, get_hardware_data, check_in, check_out

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
    return login(data)

@main_routes.route('/set-check-in', methods=['POST'])
def set_check_in():
    data = request.get_json()
    return check_in(data)

@main_routes.route('/set-check-out', methods=['POST'])
def set_check_out():
    data = request.get_json()
    return check_out(data)
