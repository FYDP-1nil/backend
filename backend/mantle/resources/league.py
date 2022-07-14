import traceback
from flask_restful import Resource
from flask import request
from backend.mantle.models.league import LeagueModel
from backend.mantle.schemas.league import LeagueSchema
from flask_jwt_extended import jwt_required
LEAGUE_NAME_ALREADY_EXISTS = "A league with that league name already exists."
FAILED_TO_CREATE = "Internal server error. Failed to create user."
league_schema = LeagueSchema()
league_list_schema = LeagueSchema(many=True)


class CreateLeague(Resource):

    @classmethod
    @jwt_required()
    def post(cls):
        league_json = request.get_json()
        league = league_schema.load(league_json)

        if LeagueModel.find_by_league_name(league.league_name):
            return {"message": LEAGUE_NAME_ALREADY_EXISTS}, 400

        try:
            league.save_to_db()
            return league_schema.dump(league), 201
            # return {"message": SUCCESS_REGISTER_MESSAGE}, 201
        except:  # failed to save user to db
            traceback.print_exc()
            # user.delete_from_db()
            return {"message": FAILED_TO_CREATE}, 500
