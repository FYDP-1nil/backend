import json
import uuid
from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt
from backend.services.gen.stats_pb2_grpc import StatsStub
from backend.services.gen.stats_pb2 import (CreateGameRequest,
    SetEventRequest, SetShotRequest, SetFoulRequest, SetOffsideRequest, SetEndGameRequest,
    Shot, Offside, Foul, GetShotsRequest, GetFoulsRequest, GetOffsidesRequest
)
from backend.services.gen.basketball_pb2 import (
CreateBasketballGameRequest, SetBasketballEventRequest, SetBasketballPointRequest, SetBasketballFoulRequest,
SetBasketballTurnoverRequest, SetBasketballReboundRequest, SetBasketballBlockRequest, SetBasketballStealRequest,
SetBasketballGameEndRequest, GetThreePointPercentageRequest, GetTotalStealsByTeamRequest, GetFreeThrowsMadeRequest,
GetTotalTurnoversByTeamRequest, GetFieldGoalPercentageRequest
)
from backend.services.gen.gridiron_pb2 import (
CreateGridironGameRequest, SetGridironEventRequest, SetGridironRushRequest, SetGridironGameEndRequest, SetGridironThrowRequest,
SetGridironKickRequest, GetTotalRushingYardsRequest, GetTotalPassingYardsRequest,
GetAvgYardsPerPlayRequest, GetTotalTouchdownsRequest, GetTotalTurnoversRequest
)

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
        return event_type in ('throw', 'rush', 'flag', 'kick', 'safety', 'turnover', 'timeout', 'end')


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

        if game_type == "soccer":
            stats_request = CreateGameRequest(leagueId=league_id, homeTeam=home_team, awayTeam=away_team)
            stats_response = stats_client.CreateGame(
                stats_request
            )
        elif game_type == "basketball":
            stats_request = CreateBasketballGameRequest(homeTeam=home_team, awayTeam=away_team, leagueId=league_id)
            stats_response = stats_client.CreateBasketballGame(
                stats_request
            )
        else:
            # american football
            stats_request = CreateGridironGameRequest(homeTeam=home_team, awayTeam=away_team, leagueId=league_id)
            stats_response = stats_client.CreateGridironGame(
                stats_request
            )

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

        else:

            # american football
            success = None
            game_id = game_event_json.get("game_id")
            play_type = game_event_json.get("event_type")

            if not validate_event_type(play_type, "gridiron"):
                return {"message": INVALID_EVENT_TYPE}, 404

            event = game_event_json.get("event")
            period = event.get("period")
            team_for = event.get("team_for")
            team_against = event.get("team_against")

            event_request = SetGridironEventRequest(gameId=game_id, playType=play_type, period=period,
                                                    teamFor=team_for, teamAgainst=team_against)
            event_response = stats_client.SetGridironEvent(
                event_request
            )
            event_id = event_response.eventId
            if play_type == "rush":
                player = event.get("player")
                yard = event.get("yard")
                result = event.get("result")
                rush_request = SetGridironRushRequest(
                    eventId=event_id,
                    player=player,
                    yard=yard,
                    result=result,
                )
                rush_response = stats_client.SetGridironRush(
                    rush_request
                )
                success = rush_response.success
            elif play_type == "throw":
                # player = event.get("player")
                player_throwing = event.get("player_throwing")
                player_receiving = event.get("player_receiving")
                yard = event.get("yard")
                result = event.get("result")
                throw_request = SetGridironThrowRequest(
                    eventId=event_id,
                    # player=player,
                    playerThrowing=player_throwing,
                    playerReceiving=player_receiving,
                    yard=yard,
                    result=result
                )
                throw_response = stats_client.SetGridironThrow(
                    throw_request
                )
                success = throw_response.success
            elif play_type == "kick":
                player = event.get("player")
                yard = event.get("yard")
                result = event.get("result")
                kick_request = SetGridironKickRequest(
                    eventId=event_id,
                    player=player,
                    yard=yard,
                    result=result,
                )
                kick_response = stats_client.SetGridironKick(
                    kick_request
                )
                success = kick_response.success
            elif play_type == "end":
                pts_home = event.get("pts_home")
                pts_away = event.get("pts_away")
                game_end_request = SetGridironGameEndRequest(
                    eventId=event_id,
                    ptsHome=pts_home,
                    ptsAway=pts_away
                )
                game_end_response = stats_client.SetGridironGameEnd(
                    game_end_request
                )
                success = game_end_response.success
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
        elif game_type == "basketball":
            get_fieldsgoals_percentage_req = GetFieldGoalPercentageRequest(gameId=str(game_id))
            get_fieldsgoals_percentage_resp = stats_client.GetFieldGoalPercentage(
                get_fieldsgoals_percentage_req
            )
            get_threepoint_percentage_req = GetThreePointPercentageRequest(gameId=str(game_id))
            get_threepoint_percentage_resp = stats_client.GetThreePointPercentage(
                get_threepoint_percentage_req
            )
            get_freethrows_req = GetFreeThrowsMadeRequest(gameId=str(game_id))
            get_freethrows_resp = stats_client.GetFreeThrowsMade(
                get_freethrows_req
            )
            get_turnovers_team_req = GetTotalTurnoversByTeamRequest(gameId=str(game_id))
            get_turnovers_team_resp = stats_client.GetTotalTurnoversByTeam(
                get_turnovers_team_req
            )
            get_total_steals_req = GetTotalStealsByTeamRequest(gameId=str(game_id))
            get_total_steals_resp = stats_client.GetTotalStealsByTeam(
                get_total_steals_req
            )

            fieldgoals_percentage_home, fieldgoals_percentage_away = get_fieldsgoals_percentage_resp.teamForStat, get_fieldsgoals_percentage_resp.teamAgainstStat
            threepoint_percentage_home, threepoint_percentage_away = get_threepoint_percentage_resp.teamForStat, get_threepoint_percentage_resp.teamAgainstStat
            freethrow_mades_home, freethrow_mades_away = get_freethrows_resp.teamForStat, get_freethrows_resp.teamAgainstStat
            turnovers_team_home, turnovers_team_away = get_turnovers_team_resp.teamForStat, get_turnovers_team_resp.teamAgainstStat
            total_steals_home, total_steals_away = get_total_steals_resp.teamForStat, get_total_steals_resp.teamAgainstStat

            payload = {
                "team1": {
                    "fieldgoals_percentage": round(fieldgoals_percentage_home, 2) * 100,
                    "threepoint_percentage": round(threepoint_percentage_home, 2) * 100,
                    "freethrow_mades": round(freethrow_mades_home, 2) * 100,
                    "turnovers": turnovers_team_home,
                    "total_steals": total_steals_home
                },
                "team2": {
                    "fieldgoals_percentage": round(fieldgoals_percentage_away, 2) * 100,
                    "threepoint_percentage": round(threepoint_percentage_away, 2) * 100,
                    "freethrow_mades": round(freethrow_mades_away, 2) * 100,
                    "turnovers": turnovers_team_away,
                    "total_steals": total_steals_away
                }
            }
        else:
            get_total_rushing_yards_req = GetTotalRushingYardsRequest(gameId=str(game_id))
            get_total_rushing_yards_resp = stats_client.GetTotalRushingYards(
                get_total_rushing_yards_req
            )
            get_total_passing_yards_req = GetTotalPassingYardsRequest(gameId=str(game_id))
            get_total_passing_yards_resp = stats_client.GetTotalPassingYards(
                get_total_passing_yards_req
            )
            get_avg_yards_play_req = GetAvgYardsPerPlayRequest(gameId=str(game_id))
            get_avg_yards_play_resp = stats_client.GetAvgYardsPerPlay(
                get_avg_yards_play_req
            )
            get_total_touchdown_req = GetTotalTouchdownsRequest(gameId=str(game_id))
            get_total_touchdown_resp = stats_client.GetTotalTouchdowns(
                get_total_touchdown_req
            )
            get_total_turnover_req = GetTotalTurnoversRequest(gameId=str(game_id))
            get_total_turnover_resp = stats_client.GetTotalTurnovers(
                get_total_turnover_req
            )

            total_rushing_yards_home, total_rushing_yards_away = get_total_rushing_yards_resp.homeTeamResponse,get_total_rushing_yards_resp.awayTeamResponse
            total_passing_yards_home, total_passing_yards_away = get_total_passing_yards_resp.homeTeamResponse,get_total_passing_yards_resp.awayTeamResponse
            avg_yards_play_home, avg_yards_play_away = get_avg_yards_play_resp.homeTeamResponse,get_avg_yards_play_resp.awayTeamResponse
            total_touchdown_home, total_touchdown_away = get_total_touchdown_resp.homeTeamResponse,get_total_touchdown_resp.awayTeamResponse
            total_turnover_home, total_turnover_away = get_total_turnover_resp.homeTeamResponse,get_total_turnover_resp.awayTeamResponse

            payload = {
                "team1": {
                    "total_rushing_yards": total_rushing_yards_home,
                    "total_passing_yards": total_passing_yards_home,
                    "avg_yards_play": avg_yards_play_home,
                    "total_touchdown": total_touchdown_home,
                    "total_turnover": total_turnover_home,
                },
                "team2": {
                    "total_rushing_yards": total_rushing_yards_away,
                    "total_passing_yards": total_passing_yards_away,
                    "avg_yards_play": avg_yards_play_away,
                    "total_touchdown": total_touchdown_away,
                    "total_turnover": total_turnover_away,
                }
            }
        
        return {"stats": payload}, 200
