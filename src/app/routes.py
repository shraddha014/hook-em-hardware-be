from flask import Blueprint
from flask_cors import CORS
from .hardware import hardware_data

main_routes = Blueprint('main_routes', __name__)
CORS(main_routes)

@main_routes.route('/hardware')
def home():
    return hardware_data()

