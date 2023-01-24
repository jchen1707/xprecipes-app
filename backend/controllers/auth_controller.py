from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from  backend.models import User,Token

class Login(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help='Username is required')
    parser.add_argument('password', type=str, required=True, help='Password is required')

    def post(self):
        data = Login.parser.parse_args()
        user = User.query.filter_by(username=data['username']).first()

        if user and user.check_password(data['password']):
            access_token = create_access_token(identity=user.id)
            token = Token(user_id=user.id, token=access_token)
            token.save()
            return{'access_token': access_token}, 200
        return {'message': 'Invalid username or password'}, 401

class Logout(Resource):

    def post(self):
        current_user = get_jwt_identity()
        token = Token.query.filter_by(user_id=current_user).first()
        token.revoked = True
        token.save
        return {'message': 'Successfully logged out'}, 200