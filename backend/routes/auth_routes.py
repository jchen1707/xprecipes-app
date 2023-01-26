from flask import Blueprint
from backend.controllers.auth_controller import Login, Logout, Register

auth_bp = Blueprint("auth_bp", __name__)
Register_instance = Register()
Login_instance = Login()
Logout_instance = Logout() 

@auth_bp.route("/register", methods=["POST"])
def register():
    return Register_instance .post()

@auth_bp.route("/login", methods=["POST"])
def login():
    return Login_instance.post()

@auth_bp.route("/logout", methods=["POST"])
def logout():
    return Logout_instance.post()
