import json
import uuid
from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt
from backend.services.gen.stats_pb2_grpc import StatsStub
from backend.services.gen.stats_pb2 import CreateGameRequest, CreateBasketballGameRequest, SetEventRequest, \
    SetBasketballEventRequest, SetBasketballPointRequest, SetBasketballFoulRequest, SetBasketballTurnoverRequest, \
    SetShotRequest, SetFoulRequest, \
    SetBasketballReboundRequest, SetBasketballBlockRequest, SetBasketballStealRequest, SetBasketballGameEndRequest, \
    SetOffsideRequest, SetEndGameRequest, Shot, Offside, Foul
from backend.services.gen.stats_pb2 import GetShotsRequest, GetFoulsRequest, GetOffsidesRequest
from backend.services.mantle.channels.stats_channel import channel

INVALID_EVENT_TYPE = "Invalid event type"
INVALID_GAME_TYPE = "Invalid game type"
stats_client = StatsStub(channel)


def validate_game_type(game_type: str) -> bool:
    return game_type in ("soccer", "basketball", "gridiron")


def validate_event_type(event_type: str, game_type: str) -> bool:
    if game_type == "soccer":
        return event_type in ("shot", "foul", "offside", "end")
    elif game_type == "basketball":
        return event_type in ('point', 'foul', 'turnover', 'end', 'block', 'steal', 'rebound')
    else:
        return True


class CreateGame(Resource):
    @classmethod
    @jwt_required()
    def post(cls, game_type: str):

        if not validate_game_type(game_type):
            return {"message": INVALID_GAME_TYPE}, 400

        game_json = request.get_json()

        league_id = game_json.get("league_id")
        home_team = game_json.get("home_team")
        away_team = game_json.get("away_team")
        stats_response = None

        if game_type == "soccer":
            stats_request = CreateGameRequest(leagueId=league_id, homeTeam=home_team, awayTeam=away_team)
            stats_response = stats_client.CreateGame(
                stats_request
            )
        elif game_type == "basketball":
            stats_request = CreateBasketballGameRequest(leagueId=league_id, homeTeam=home_team, awayTeam=away_team)
            stats_response = stats_client.CreateBasketballGame(
                stats_request
            )
        else:
            # american football
            pass

        return {"game_id": stats_response.gameId}, 200


class GameEvents(Resource):
    @classmethod
    @jwt_required()
    def post(cls, game_type: str):

        if not validate_game_type(game_type):
            return {"message": INVALID_GAME_TYPE}, 400

        game_event_json = request.get_json()

        if game_type == "soccer":

            success = None
            game_id = game_event_json.get("game_id")
            event_type = game_event_json.get("event_type")

            if not validate_event_type(event_type, "soccer"):
                return {"message": INVALID_EVENT_TYPE}, 404

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
                shot_request = SetShotRequest(
                    gameId=game_id,
                    teamFor=team_for,
                    teamAgainst=team_against,
                    shotDetails=Shot(
                        isGoal=is_goal,
                        isOnTarget=is_on_target,
                        scorer=scorer,
                        assist=assist,
                        time=time_
                    )
                )
                shot_response = stats_client.SetShot(
                    shot_request
                )
                success = shot_response.success
            elif event_type == "foul":
                is_yellow = event.get("is_yellow")
                is_red = event.get("is_red")
                player = event.get("player")
                reason = event.get("reason")
                time_ = int(event.get("time"))
                foul_request = SetFoulRequest(
                    gameId=game_id,
                    teamFor=team_for,
                    teamAgainst=team_against,
                    foulDetails=Foul(
                        isYellow=is_yellow,
                        isRed=is_red,
                        player=player,
                        reason=reason,
                        time=time_
                    )
                )
                foul_response = stats_client.SetFoul(
                    foul_request
                )
                success = foul_response.success
            elif event_type == "offside":
                time_ = int(event.get("time"))
                offside_request = SetOffsideRequest(
                    gameId=game_id,
                    teamFor=team_for,
                    teamAgainst=team_against,
                    offsideDetails=Offside(
                        time=time_
                    )
                )
                offside_response = stats_client.SetOffside(
                    offside_request
                )
                success = offside_response.success
            elif event_type == "end":
                endgame_request = SetEndGameRequest(
                    gameId=game_id,
                    goalsHome=event.get("goals_home"),
                    goalsAway=event.get("goals_away")
                )
                endgame_response = stats_client.SetEndGame(
                    endgame_request
                )
                success = endgame_response.success
            else:
                return {"message": INVALID_EVENT_TYPE}, 404
            return {"success": success and is_event_success}, 200

        elif game_type == "basketball":

            success = None
            game_id = game_event_json.get("game_id")
            play_type = game_event_json.get("event_type")

            if not validate_event_type(play_type, "basketball"):
                return {"message": INVALID_EVENT_TYPE}, 404

            event = game_event_json.get("event")
            period = event.get("period")
            team_for = event.get("team_for")
            team_against = event.get("team_against")

            event_request = SetBasketballEventRequest(gameId=game_id, playType=play_type, period=period,
                                                      teamFor=team_for, teamAgainst=team_against)
            event_response = stats_client.SetBasketballEvent(
                event_request
            )
            event_id = event_response.eventId
            if play_type == "point":
                player = event.get("player")
                assist = event.get("assist")
                result = event.get("result")
                point = event.get("point")
                point_request = SetBasketballPointRequest(
                    eventId=event_id,
                    player=player,
                    assist=assist,
                    result=result,
                    point=point
                )
                point_response = stats_client.SetBasketballPoint(
                    point_request
                )
                success = point_response.success
            elif play_type == "foul":
                player = event.get("player")
                reason = event.get("reason")
                foul_request = SetBasketballFoulRequest(
                    eventId=event_id,
                    player=player,
                    reason=reason
                )
                foul_response = stats_client.SetBasketballFoul(
                    foul_request
                )
                success = foul_response.success
            elif play_type == "turnover":
                player = event.get("player")
                turnover_request = SetBasketballTurnoverRequest(
                    eventId=event_id,
                    player=player
                )
                turnover_response = stats_client.SetBasketballTurnover(
                    turnover_request
                )
                success = turnover_response.success
            elif play_type == "rebound":
                player = event.get("player")
                rebound_request = SetBasketballReboundRequest(
                    eventId=event_id,
                    player=player
                )
                rebound_response = stats_client.SetBasketballRebound(
                    rebound_request
                )
                success = rebound_response.success
            elif play_type == "block":
                player = event.get("player")
                block_request = SetBasketballBlockRequest(
                    eventId=event_id,
                    player=player
                )
                block_response = stats_client.SetBasketballBlock(
                    block_request
                )
                success = block_response.success
            elif play_type == "steal":
                player = event.get("player")
                steal_request = SetBasketballStealRequest(
                    eventId=event_id,
                    player=player
                )
                steal_response = stats_client.SetBasketballSteal(
                    steal_request
                )
                success = steal_response.success
            elif play_type == "end":
                pts_home = event.get("pts_home")
                pts_away = event.get("pts_away")
                end_request = SetBasketballGameEndRequest(
                    eventId=event_id,
                    ptsHome=pts_home,
                    ptsAway=pts_away
                )
                end_response = stats_client.SetBasketballGameEnd(
                    end_request
                )
                success = end_response.success

            return {"event_id": event_id, "success": success}, 200


class GameStats(Resource):
    @classmethod
    @jwt_required()
    def post(cls, game_type: str, game_id: uuid):
        payload = {}
        if game_type == "soccer":
            shots_req = GetShotsRequest(gameId=str(game_id))
            shots_resp = stats_client.GetShots(
                shots_req
            )
            fouls_req = GetFoulsRequest(gameId=str(game_id))
            fouls_resp = stats_client.GetFouls(
                fouls_req
            )
            offsides_req = GetOffsidesRequest(gameId=str(game_id))
            offsides_resp = stats_client.GetOffsides(
                offsides_req
            )
            team1_shots, team2_shots = shots_resp.teamFor, shots_resp.teamAgainst
            # team1_fouls, team2_fouls = [], []
            team1_fouls, team2_fouls = fouls_resp.teamFor, fouls_resp.teamAgainst
            team1_offsides, team2_offsides = offsides_resp.teamFor, offsides_resp.teamAgainst
            count_team1_shots, count_team1_fouls, count_team1_goals, count_team1_shots_target, count_team_1_yellow, count_team_1_red, count_team1_offsides = len(
                team1_shots), len(team1_fouls), 0, 0, 0, 0, len(team1_offsides)
            count_team2_shots, count_team2_fouls, count_team2_goals, count_team2_shots_target, count_team_2_yellow, count_team_2_red, count_team2_offsides = len(
                team2_shots), len(team2_fouls), 0, 0, 0, 0, len(team2_offsides)

            for team1_shot in team1_shots:
                if team1_shot.isOnTarget:
                    count_team1_shots_target += 1
                if team1_shot.isGoal:
                    count_team1_goals += 1

            for team2_shot in team2_shots:
                if team2_shot.isOnTarget:
                    count_team2_shots_target += 1
                if team2_shot.isGoal:
                    count_team2_goals += 1

            for team1_foul in team1_fouls:
                if team1_foul.isYellow:
                    count_team_1_yellow += 1
                if team1_foul.isRed:
                    count_team_1_red += 1

            for team2_foul in team2_fouls:
                if team2_foul.isYellow:
                    count_team_2_yellow += 1
                if team2_foul.isRed:
                    count_team_2_red += 1

            payload = {
                "team1": {
                    "goals": count_team1_goals,
                    "shots": count_team1_shots,
                    "shots_on_target": count_team1_shots_target,
                    "fouls": count_team1_fouls,
                    "yellow_cards": count_team_1_yellow,
                    "red_cards": count_team_1_red,
                    "offsides": count_team1_offsides
                },
                "team2": {
                    "goals": count_team2_goals,
                    "shots": count_team2_shots,
                    "shots_on_target": count_team2_shots_target,
                    "fouls": count_team2_fouls,
                    "yellow_cards": count_team_2_yellow,
                    "red_cards": count_team_2_red,
                    "offsides": count_team2_offsides
                }
            }
        return {"stats": payload}, 200
