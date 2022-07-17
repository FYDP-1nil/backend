import traceback
import uuid
from flask_restful import Resource
from flask import request
from backend.mantle.models.league import LeagueModel
from backend.mantle.schemas.league import LeagueSchema
from flask_jwt_extended import jwt_required
from werkzeug.security import generate_password_hash, check_password_hash
LEAGUE_NAME_ALREADY_EXISTS = "A league with that league name already exists."
FAILED_TO_CREATE = "Internal server error. Failed to create user."
league_schema = LeagueSchema()
league_list_schema = LeagueSchema(many=True)

JOIN_SUCCESS = "Successfully joined the league"
INVALID_CREDENTIALS = "Invalid credentials!"
LEAGUE_NOT_FOUND = "League does not exist"
LEAGUE_DELETED = "League deleted"

class CreateLeague(Resource):

    @classmethod
    @jwt_required()
    def post(cls):
        league_json = request.get_json()
        league = league_schema.load(league_json)

        if LeagueModel.find_by_league_name(league.league_name):
            return {"message": LEAGUE_NAME_ALREADY_EXISTS}, 400

        league.league_password = generate_password_hash(league.league_password)

        try:
            league.save_to_db()
            return league_schema.dump(league), 201
            # return {"message": SUCCESS_REGISTER_MESSAGE}, 201
        except:  # failed to save user to db
            traceback.print_exc()
            # user.delete_from_db()
            return {"message": FAILED_TO_CREATE}, 500

class LeagueLogin(Resource):
    @classmethod
    @jwt_required()
    def post(cls):
        league_json = request.get_json()
        league_data = league_schema.load(league_json)

        league = LeagueModel.find_by_league_name(league_data.league_name)

        if league and check_password_hash(league.league_password, league_data.league_password):
            return {"message": JOIN_SUCCESS}, 200

        return {"message": INVALID_CREDENTIALS}, 401

class League(Resource):
    @classmethod
    @jwt_required()
    def get(cls, league_id: uuid):
        league = LeagueModel.find_by_id(league_id)
        if not league:
            return {"message": LEAGUE_NOT_FOUND}, 404

        return league_schema.dump(league), 200

    @classmethod
    def delete(cls, league_id: uuid):
        league = LeagueModel.find_by_id(league_id)
        if not league_id:
            return {"message": LEAGUE_NOT_FOUND}, 404

        league.delete_from_db()
        return {"message": LEAGUE_DELETED}, 200

class LeagueList(Resource):
    @classmethod
    @jwt_required()
    def get(cls):
        return {"leagues": league_list_schema.dump(LeagueModel.find_all())}, 200