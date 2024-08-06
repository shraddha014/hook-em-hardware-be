# app/routes.py
from flask import Blueprint, request, jsonify
from flask_cors import CORS
from .login import login
from .hardware import set_hardware_data, get_hardware_data, check_in, check_out
from .project_list import get_user_associated_project_id
from .project_list import get_project_from_project_id
from .project_list import set_project_list_user
from .create_projects import create_project

from bson import ObjectId
import json

def jsonify_with_objectid(data):
    class JSONEncoder(json.JSONEncoder):
        def default(self, o):
            if isinstance(o, ObjectId):
                return str(o)
            return json.JSONEncoder.default(self, o)
    return json.dumps(data, cls=JSONEncoder)

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

@main_routes.route('/api/get-user-associated-project-list', methods=['GET'])
def get_projects_from_user():
    data = request.args.get('username')
    return get_user_associated_project_id(data)

@main_routes.route('/api/get_project_from_project_id', methods=['GET'])
def get_project_from_id():
    data = request.args.get('project_id')
    return get_project_from_project_id(data)

@main_routes.route('/set_project_to_user', methods=['POST'])
def set_project_list():
    data = request.get_json()
    return set_project_list_user(data)

@main_routes.route('/api/create-project', methods=['POST'])
def create_project_route():
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    project_id = data.get('projectId')
    result = create_project(name, description, project_id)
    return jsonify_with_objectid(result), 201