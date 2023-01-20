from flask import Blueprint,request,jsonify,make_response
from flask_login import login_user, logout_user
from  server.models import User


auth_controller = Blueprint('auth_controller,__name__')

def login():
    username = request.form['username']
    password = request.form['password']

    user = User.query.filter_by(username=username).first()

    if user is None or not user.check_password(password):
        return make_response(jsonify({'error':'Invalid username or password'}, 401))

    login_user(user)
    return jsonify({'result': 'success'})

def logout():
    logout_user()
    return jsonify({'result': 'success'})