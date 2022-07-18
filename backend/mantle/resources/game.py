import json
import uuid
from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt
from backend.stats.stats_pb2_grpc import StatsStub
from backend.stats.stats_pb2 import CreateGameRequest, SetEventRequest, SetShotRequest, SetFoulRequest, SetOffsideRequest
from backend.stats.stats_pb2 import GetShotsRequest
from backend.mantle.channels.stats_channel import channel

INVALID_EVENT_TYPE = "Invalid event type"
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
        game_event_json = request.get_json()
        game_id = game_event_json.get("game_id")
        event_type = game_event_json.get("event_type")
        event = game_event_json.get("event")
        event_str = json.dumps(event)
        event_request = SetEventRequest(eventType=event_type, gameId=game_id, event=event_str)
        event_response = stats_client.SetEvent(
            event_request
        )
        is_event_success = event_response.success
        team_for = event.get("team_for")
        team_against = event.get("team_against")
        if event_type == "shot":
            is_goal = event.get("is_goal")
            is_on_target = event.get("is_on_target")
            scorer = event.get("scorer")
            assist = event.get("assist")
            time_ = int(event.get("time"))
            shot_request = SetShotRequest(gameId=game_id, teamFor=team_for, teamAgainst=team_against)
            shot_response = stats_client.SetShot(
                shot_request
            )
            success = shot_response.success
        elif event_type == "foul":
            is_yellow = event.get("is_yellow")
            is_red = event.get("is_red")
            player = event.get("player")
            reason = event.get("reason")
            foul_request = SetFoulRequest()
            foul_request.gameId = game_id
            foul_request.teamFor = team_for
            foul_request.teamAgainst = team_against
            foul_details = foul_request.foulDetails.add()
            foul_details.isYellow = is_yellow
            foul_details.isRed = is_red
            foul_details.player = player
            foul_details.reason = reason
            # foul_request = SetFoulRequest(gameId=game_id, teamFor=team_for, teamAgainst=team_against)
            foul_response = stats_client.SetFoul(
                foul_request
            )
            success = foul_response.success
        elif event_type == "offside":
            time_ = int(event.get("time"))
            # offside_request = SetOffsideRequest(gameId=game_id, teamFor=team_for, teamAgainst=team_against)
            offside_request = SetOffsideRequest()
            offside_request.gameId = game_id
            offside_request.teamFor = team_for
            offside_request.teamAgainst = team_against
            offside_details = offside_request.offsideDetails.add()
            offside_details.time = time_
            offside_response = stats_client.SetOffside(
                offside_request
            )
            success = offside_response.success
        else:
            return {"message": INVALID_EVENT_TYPE}, 404
        return {"success": success and is_event_success}, 200


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
