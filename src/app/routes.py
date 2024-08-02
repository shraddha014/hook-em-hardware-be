from flask import Blueprint, request
from flask_cors import CORS
from .hardware import hardware_data
from .login import login

main_routes = Blueprint('main_routes', __name__)
CORS(main_routes)

@main_routes.route('/hardware')
def home():
    return hardware_data()

@main_routes.route('/login', methods=['POST'])
def login_route():
    return login(request.data)
