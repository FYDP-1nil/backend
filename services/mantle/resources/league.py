import traceback
import uuid
from flask_restful import Resource
from flask import request
from backend.services.mantle.models.league import LeagueModel
from backend.services.mantle.schemas.league import LeagueSchema
from flask_jwt_extended import jwt_required
from werkzeug.security import generate_password_hash, check_password_hash
from backend.services.gen.stats_pb2_grpc import StatsStub

from backend.services.mantle.channels.stats_channel import channel

from backend.services.gen.basketball_pb2 import (
    GetTopFivePlayersByPointsPerGameRequest, GetTopFivePlayersByReboundsPerGameRequest,
    GetTopFivePlayersByAssistsPerGameRequest, GetTopFivePlayersByBlocksPerGameRequest,
    GetTopFivePlayersByStealsPerGameRequest, GetTopFivePlayersByFieldGoalPercentageRequest,
    GetTopFivePlayersBy3ptPercentageRequest, GetTopFivePlayersByFreeThrowPercentageRequest
)

from backend.services.gen.gridiron_pb2 import (
    GetTopFivePlayersByRushingYardsRequest, GetTopFivePlayersByReceivingYardsRequest,
    GetTopFivePlayersByThrowingYardsRequest, GetTopFivePlayersByKicksMadeRequest,
    GetTopFivePlayersByCompletionPercentageRequest
)

stats_client = StatsStub(channel)
league_schema = LeagueSchema()
league_list_schema = LeagueSchema(many=True)

LEAGUE_NAME_ALREADY_EXISTS = "A league with that league name already exists."
FAILED_TO_CREATE = "Internal server error. Failed to create user."
JOIN_SUCCESS = "Successfully joined the league"
INVALID_CREDENTIALS = "Invalid credentials!"
LEAGUE_NOT_FOUND = "League does not exist"
LEAGUE_DELETED = "League deleted"
INVALID_SPORT = "Specified sport is invalid"


class CreateLeague(Resource):

    @classmethod
    @jwt_required()
    def post(cls):
        league_json = request.get_json()
        league = league_schema.load(league_json)

        if LeagueModel.find_by_league_name(league.league_name):
            return {"message": LEAGUE_NAME_ALREADY_EXISTS}, 400

        if league.sport not in ("soccer", "basketball", "gridiron"):
            return {"message": INVALID_SPORT}, 400

        league.league_password = generate_password_hash(league.league_password)

        try:
            league.save_to_db()
            return league_schema.dump(league), 201
        except:  # failed to save user to db
            traceback.print_exc()
            # user.delete_from_db()
            return {"message": FAILED_TO_CREATE}, 500


class LeagueLogin(Resource):
    @classmethod
    @jwt_required()
    def post(cls):
        league_json = request.get_json()

        league = LeagueModel.find_by_league_name(league_json.get("league_name"))

        if league and check_password_hash(league.league_password, league_json.get("league_password")):
            return {
                       "message": JOIN_SUCCESS,
                       "league_id": str(league.id),
                       "sport": league.sport
                   }, 200

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


class LeagueStats(Resource):
    @classmethod
    @jwt_required()
    def get(cls, league_id: str):
        league, status_code = League.get(league_id)
        sport = league.get("sport")
        if sport not in ("soccer", "basketball", "gridiron"):
            return {"message": INVALID_SPORT}, 400
        if sport == "basketball":

            return_response = []
            response = {"Points Per Game": stats_client.GetTopFivePlayersByPointsPerGame(
                GetTopFivePlayersByPointsPerGameRequest(leagueId=league_id)
            ).resp, "Rebounds Per Game": stats_client.GetTopFivePlayersByReboundsPerGame(
                GetTopFivePlayersByReboundsPerGameRequest(leagueId=league_id)
            ).resp, "Assists Per Game": stats_client.GetTopFivePlayersByAssistsPerGame(
                GetTopFivePlayersByAssistsPerGameRequest(leagueId=league_id)
            ).resp, "Blocks Per Game": stats_client.GetTopFivePlayersByBlocksPerGame(
                GetTopFivePlayersByBlocksPerGameRequest(leagueId=league_id)
            ).resp, "Steals Per Game": stats_client.GetTopFivePlayersByStealsPerGame(
                GetTopFivePlayersByStealsPerGameRequest(leagueId=league_id)
            ).resp, "Field Goal Percentage": stats_client.GetTopFivePlayersByFieldGoalPercentage(
                GetTopFivePlayersByFieldGoalPercentageRequest(leagueId=league_id)
            ).resp, "3pt Percentage": stats_client.GetTopFivePlayersBy3ptPercentage(
                GetTopFivePlayersBy3ptPercentageRequest(leagueId=league_id)
            ).resp, "Free throw Percentage": stats_client.GetTopFivePlayersByFreeThrowPercentage(
                GetTopFivePlayersByFreeThrowPercentageRequest(leagueId=league_id)
            ).resp}

            percentage_fields = ("Free throw Percentage", "3pt Percentage", "Field Goal Percentage")
            for key, value in response.items():
                resp = {"name": key, "players": []}
                for stat_resp in value:
                    stat_val = round(stat_resp.stat, 2) * 100 if key in percentage_fields else round(stat_resp.stat, 2)
                    dict_ = {
                        stat_resp.playerName: stat_val
                    }
                    resp["players"].append(dict_)
                return_response.append(resp)

            return return_response

        elif sport == "soccer":
            pass
        else:

            return_response = []
            response = {"Total Rushing Yards": stats_client.GetTopFivePlayersByRushingYards(
                GetTopFivePlayersByRushingYardsRequest(leagueId=league_id)
            ).resp, "Total Receiving Yards": stats_client.GetTopFivePlayersByReceivingYards(
                GetTopFivePlayersByReceivingYardsRequest(leagueId=league_id)
            ).resp, "Total Throwing Yards": stats_client.GetTopFivePlayersByThrowingYards(
                GetTopFivePlayersByThrowingYardsRequest(leagueId=league_id)
            ).resp, "Total Kicks Made": stats_client.GetTopFivePlayersByKicksMade(
                GetTopFivePlayersByKicksMadeRequest(leagueId=league_id)
            ).resp, "Completion %": stats_client.GetTopFivePlayersByCompletionPercentage(
                GetTopFivePlayersByCompletionPercentageRequest(leagueId=league_id)
            ).resp}

            percentage_fields = ("Completion %")
            for key, value in response.items():
                resp = {"name": key, "players": []}
                for stat_resp in value:
                    stat_val = round(stat_resp.stat, 2) * 100 if key in percentage_fields else round(stat_resp.stat, 2)
                    dict_ = {
                        stat_resp.playerName: stat_val
                    }
                    resp["players"].append(dict_)
                return_response.append(resp)

            return return_response


class LeagueList(Resource):
    @classmethod
    @jwt_required()
    def get(cls):
        return {"leagues": league_list_schema.dump(LeagueModel.find_all())}, 200
