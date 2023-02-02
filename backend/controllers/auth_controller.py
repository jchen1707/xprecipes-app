from flask import request
from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from cerberus import Validator
from backend.models import User, Token
from backend import db
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

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

class Register(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("username", type=str, required=True, help="Username is required")
    parser.add_argument("password", type=str, required=True, help="Password is required")

    def post(self):
        data = request.get_json()
        v = Validator(validation_schema)
        if not v.validate(data):
            return v.errors, 400
        if User.query.filter_by(username=data["username"]).first():
            return {"message": "Username already exists"}, 400
        username = data.get("username")
        password = data.get("password")
        hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return {"message": "New user created!"}, 201

class Login(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("username", type=str, required=True, help="Username is required")
    parser.add_argument("password", type=str, required=True, help="Password is required")

    def post(self):
        data = Login.parser.parse_args()
        v = Validator(validation_schema)
        if not v.validate(data):
            return v.errors, 400
        user = User.query.filter_by(username=data["username"]).first()
        if user and bcrypt.check_password_hash(user.password, data["password"]):
            access_token = create_access_token(identity=user.id)
            token = Token(user_id=user.id, token=access_token)
            db.session.add(token)
            db.session.commit()
            return {"access_token": access_token}, 200
        return {"message": "Invalid username or password"}, 400

class Logout(Resource):
    @jwt_required
    def post(self):
        current_user = get_jwt_identity()
        if current_user is None:
            return {"message": "Unauthorized access"}, 401
        token = Token.query.filter_by(user_id=current_user).first()
        if token:
            token.revoked = True
            db.session.commit()
            return {"message": "Successfully logged out"}, 200
        return {"message": "Invalid token or user not found"}, 401

