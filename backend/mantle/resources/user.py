import traceback
from flask_restful import Resource
from flask import request
from flask_jwt_extended import create_access_token
from models.user import UserModel
from schemas.user import UserSchema
from werkzeug.security import generate_password_hash, check_password_hash

USER_ALREADY_EXISTS = "A user with that username already exists."
EMAIL_ALREADY_EXISTS = "A user with that email already exists."
USER_NOT_FOUND = "User not found."
USER_DELETED = "User deleted."
INVALID_CREDENTIALS = "Invalid credentials!"
FAILED_TO_CREATE = "Internal server error. Failed to create user."
SUCCESS_REGISTER_MESSAGE = "Account created successfully"
user_schema = UserSchema()
user_list_schema = UserSchema(many=True)


class UserRegister(Resource):
    @classmethod
    def post(cls):
        user_json = request.get_json()
        user = user_schema.load(user_json)

        if UserModel.find_by_username(user.username):
            return {"message": USER_ALREADY_EXISTS}, 400

        if UserModel.find_by_email(user.email):
            return {"message": EMAIL_ALREADY_EXISTS}, 400

        user.password = generate_password_hash(user.password)
        try:
            user.save_to_db()
            return {"message": SUCCESS_REGISTER_MESSAGE}, 201
        except:  # failed to save user to db
            traceback.print_exc()
            user.delete_from_db()
            return {"message": FAILED_TO_CREATE}, 500


class User(Resource):
    @classmethod
    def get(cls, user_id: int):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {"message": USER_NOT_FOUND}, 404

        return user_schema.dump(user), 200

    @classmethod
    def delete(cls, user_id: int):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {"message": USER_NOT_FOUND}, 404

        user.delete_from_db()
        return {"message": USER_DELETED}, 200


class UserLogin(Resource):
    @classmethod
    def post(cls):
        user_json = request.get_json()
        user_data = user_schema.load(user_json, partial=("email",))

        user = UserModel.find_by_username(user_data.username)

        if user and check_password_hash(user.password, user_data.password):
            access_token = create_access_token(identity=user.id, fresh=True)
            user.access_token = access_token
            user.save_to_db()
            return {"access_token": access_token}, 200

        return {"message": INVALID_CREDENTIALS}, 401


class UserList(Resource):
    @classmethod
    def get(cls):
        return {"users": user_list_schema.dump(UserModel.find_all())}, 200
