import traceback
from flask_restful import Resource
from flask import request
from backend.mantle.models.game import GameModel
from backend.mantle.schemas.game import GameSchema
from flask_jwt_extended import jwt_required
LEAGUE_NAME_ALREADY_EXISTS = "A league with that league name already exists."
FAILED_TO_CREATE = "Internal server error. Failed to create user."
league_schema = GameSchema()
league_list_schema = GameSchema(many=True)


class CreateGame(Resource):

    @classmethod
    # @jwt_required()
    def post(cls):
        return {"message": "dummy"}, 201