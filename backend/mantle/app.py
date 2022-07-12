import os
from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager
from marshmallow import ValidationError
from db import db
from ma import ma
from http import HTTPStatus
from resources.user import UserRegister, UserLogin, User, UserList
from dotenv import load_dotenv
from flask_migrate import Migrate

load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"] = True
app.secret_key = os.environ.get("APP_SECRET_KEY")
api = Api(app)


@app.before_first_request
def create_tables():
    """
    Helper method to create the required tables before the first request
    """
    db.create_all()


@app.errorhandler(ValidationError)
def handle_marshmallow_validation(err):
    """
    Helper method to handle marshmallow validation errors and convert them to a
    json object
    """
    return jsonify(err.messages), HTTPStatus.BAD_REQUEST


migrate = Migrate(app, db)
jwt = JWTManager(app)
db.init_app(app)

# add endpoints
api.add_resource(UserRegister, "/users/create")
api.add_resource(User, "/user/<int:user_id>")
api.add_resource(UserList, "/users")
api.add_resource(UserLogin, "/login")

if __name__ == "__main__":
    # db.init_app(app)
    ma.init_app(app)
    app.run(host='0.0.0.0', port=3000)
