from flask import Blueprint
from backend.controllers.auth_controller import Login, Logout
from backend.app import csrf
from backend.controllers.auth_controller import AuthController

auth_bp = Blueprint('auth_bp', __name__)


@auth_bp.route('/register', methods=['POST'])
@csrf.exempt
def register():
    return AuthController.register()


@auth_bp.route('/login', methods=['POST'])
@csrf.exempt
def login():
    return Login.post()

@auth_bp.route('/logout', methods=['POST'])
@csrf.exempt
def logout():
    return Logout.post()
