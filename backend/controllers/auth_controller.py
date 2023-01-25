from flask import request
from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from flask_wtf.csrf import validate_csrf
from cerberus import Validator
from  backend.models import User,Token
from .__init__ import db


class Register(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        
        # Hash the password with a salt
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        
        # Create a new user
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return ({'message': 'New user created!'}), 201

class Login(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help='Username is required')
    parser.add_argument('password', type=str, required=True, help='Password is required')

    def post(self):
        if not validate_csrf(request.form.get("csrf_token")):
            return {"message": "Invalid CSRF token"}, 400
        data = Login.parser.parse_args()
        v = Validator(validation_schema)
        if not v.validate(data):
            return v.errors, 400
        user = User.query.filter_by(username=data['username']).first()
        if user and user.check_password(data['password']):
            access_token = create_access_token(identity=user.id)
            token = Token(user_id=user.id, token=access_token)
            token.save()
            return{'access_token': access_token}, 200
        return {'message': 'Invalid username or password'}, 401

class Logout(Resource):
    @jwt_required
    def post(self):
        current_user = get_jwt_identity()
        if current_user is None:
            return {'message': 'Unauthorized access'}, 401
        token = Token.query.filter_by(user_id=current_user).first()
        token.revoked = True
        token.save()
        return {'message': 'Successfully logged out'}, 200

validation_schema = {
    "username": {
        "type": "string",
        "required": True
    },
    "password": {
        "type": "string",
        "required": True,
        "minlength": 8
    }
}