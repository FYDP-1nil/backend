import uuid
from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt
from backend.stats.stats_pb2_grpc import StatsStub
from backend.stats.stats_pb2 import CreateGameRequest
from backend.stats.stats_pb2 import GetShotsRequest
from backend.mantle.channels.stats_channel import channel

stats_client = StatsStub(channel)

class CreateGame(Resource):
    @classmethod
    @jwt_required()
    def post(cls):
        game_json = request.get_json()
        home_team = game_json.get("home_team")
        away_team = game_json.get("away_team")
        user_id = get_jwt().get("sub")
        stats_request = CreateGameRequest(homeTeam=home_team, awayTeam=away_team, userId=user_id)
        stats_response = stats_client.CreateGame(
            stats_request
        )
        return {"game_id": stats_response.gameId}, 200


class GameEvents(Resource):
    @classmethod
    @jwt_required()
    def post(cls):
        return {"message": "game events endpoint"}, 200


class GameStats(Resource):
    @classmethod
    @jwt_required()
    def post(cls, game_type: str, game_id: uuid):
        success = "0"
        if game_type == "Soccer":
            event_req = GetShotsRequest(gameId="1")
            event_resp = stats_client.GetShots(
                event_req
            )
            success = "1"
            print(event_resp.TeamShots.shots)
        return {"message": success + "game stats endpoint"}, 200
