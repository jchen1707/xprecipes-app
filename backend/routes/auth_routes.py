from flask import Blueprint, jsonify, request
from backend.controllers import auth_controller
from backend import csrf_validation_middleware
auth_bp = Blueprint("auth_bp", __name__)

controller = auth_controller()

@auth_bp.before_request
def csrf_validation():
    csrf_validation_middleware()

@auth_bp.route("/auth/register", methods=["POST"])
def register():
    response = controller.register(request.get_json())
    return jsonify(response), response["status_code"]

@auth_bp.route("/auth/login", methods=["POST"])
def login():
    response = controller.login(request.get_json())
    return jsonify(response), response["status_code"]

@auth_bp.route("/auth/logout", methods=["POST"])
def logout():
    response = controller.logout()
    return jsonify(response), response["status_code"]
