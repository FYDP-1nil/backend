from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt
from backend.stats.stats_pb2_grpc import StatsStub
from backend.stats.stats_pb2 import CreateGameRequest
from backend.mantle.channels.stats_channel import channel
LEAGUE_NAME_ALREADY_EXISTS = "A league with that league name already exists."
FAILED_TO_CREATE = "Internal server error. Failed to create user."

stats_client = StatsStub(channel)

class CreateGame(Resource):

    @classmethod
    @jwt_required()
    def post(cls):
        game_json = request.get_json()
        home_team = game_json.get("homeTeam")
        away_team = game_json.get("awayTeam")
        user_id = get_jwt().get("sub")
        stats_request = CreateGameRequest(homeTeam=home_team, awayTeam=away_team, userId=user_id)
        stats_response = stats_client.CreateGame(
            stats_request
        )
        return {"game_id": stats_response.gameId}, 200

