import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field can not be blank"
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field can not be blank")

    def post(self):

        data = UserRegister.parser.parse_args()
        user = UserModel.get_user_by_username(data['username'])
        if user:
            return {"message": "User is already added"}, 400

        new_user: UserModel = UserModel(**data)
        new_user.save_to_db()

        return {"message": "You have registered successfully"}, 201
