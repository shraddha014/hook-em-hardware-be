# app/routes.py
from flask import Blueprint, request
from flask_cors import CORS
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

@main_routes.route('/set-check-in', methods=['POST'])
def set_check_in():
    data = request.get_json()
    return check_in(data)

@main_routes.route('/set-check-out', methods=['POST'])
def set_check_out():
    data = request.get_json()
    return check_out(data)
