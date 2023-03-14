import os
import grpc

from services.gen import stats_pb2 
from services.gen.stats_pb2_grpc import StatsStub
from services.gen import basketball_pb2
import uuid

host = os.getenv("GRPC_HOST", "localhost")
channel = grpc.insecure_channel(f"{host}:50052")
stats_client = StatsStub(channel)

# test createGame
# res = stats_client.CreateGame(stats_pb2.CreateGameRequest(homeTeam="Chelsea", awayTeam="Madrid"))
# print("this is comiung from db: ", res)
# gameId = res.gameId

# # test setShot 1 
# print("test shot 1?: ", stats_client.SetShot(stats_pb2.SetShotRequest(
#     gameId = gameId, 
#     teamFor = "Chelsea",
#     teamAgainst = "Madrid",
#     shotDetails = stats_pb2.Shot(
#         isGoal= True,
#         isOnTarget = True, 
#         scorer = "messi",
#         assist = "ronald",
#         time = 45 
#     ) 
# )))

# # test setShot 2
# print("test shot 2?: ", stats_client.SetShot(stats_pb2.SetShotRequest(
#     gameId = gameId, 
#     teamFor = "Madrid",
#     teamAgainst = "Chelsea",
#     shotDetails = stats_pb2.Shot(
#         isGoal= True,
#         isOnTarget = True, 
#         scorer = "ronaldo",
#         assist = "pele",
#         time = 90
#     ) 
# )))

# # test setShot 3
# print("test shot 3?: ", stats_client.SetShot(stats_pb2.SetShotRequest(
#     gameId = gameId, 
#     teamFor = "Madrid",
#     teamAgainst = "Chelsea",
#     shotDetails = stats_pb2.Shot(
#         isGoal= True,
#         isOnTarget = True, 
#         scorer = "asd",
#         assist = "salah",
#         time = 90
#     ) 
# )))

# # test foul
# print("test foul 1?: ", stats_client.SetFoul(stats_pb2.SetFoulRequest(
#     gameId = gameId, 
#     teamFor = "Madrid",
#     teamAgainst = "Chelsea",
#     foulDetails = stats_pb2.Foul(
#         isYellow=True,
#         isRed=True,
#         player="Iram",
#         reason="Shreyas",
#         time = 10
#     ) 
# )))

# # test foul 2
# print("test foul 2?: ", stats_client.SetFoul(stats_pb2.SetFoulRequest(
#     gameId = gameId, 
#     teamFor = "Chelsea",
#     teamAgainst = "Madrid",
#     foulDetails = stats_pb2.Foul(
#         isYellow=False,
#         isRed=True,
#         player="Banin",
#         reason="madhur",
#         time = 15
#     ) 
# )))

# print("test offside: ", stats_client.SetOffside(stats_pb2.SetOffsideRequest(
#     gameId = gameId, 
#     teamFor = "Chelsea",
#     teamAgainst = "Madrid",
#     offsideDetails = stats_pb2.Offside(
#         time=10
#     ) 
# )))

# # test setEvent
# print("test event: ", stats_client.SetEvent(stats_pb2.SetEventRequest(
#     eventType = "testtype", 
#     gameId = gameId,
#     event = "json blob"
# )))

# # test getShots
# resp = stats_client.GetShots(stats_pb2.GetShotsRequest(
#     gameId = gameId
# ))

# shotsFromHomeTeam = resp.teamFor
# shotsFromAwayTeam = resp.teamAgainst
# print("home team shots: ", shotsFromHomeTeam)
# print("away team shots: ", shotsFromAwayTeam)

# print("fouls", stats_client.GetFouls(stats_pb2.GetFoulsRequest(
#     gameId=gameId
# )))

# print("offsides", stats_client.GetOffsides(stats_pb2.GetOffsidesRequest(
#     gameId=gameId
# )))

# test create basketball game
# print("create baskestball game", stats_client.CreateBasketballGame(basketball_pb2.CreateBasketballGameRequest(
#     leagueId="f57bc453-1e2b-44f4-8ef0-c5baa4a76e37", homeTeam="home", awayTeam="away"
# )))

# create test basketball event
# resp = stats_client.SetBasketballEvent(basketball_pb2.SetBasketballEventRequest(
#     gameId="b42f749b-4501-481b-82d8-7c9fadb1bd38", 
#     playType="point", 
#     period="1", 
#     teamFor="skibidy", 
#     teamAgainst="bap"
# ))
# print("create basketball event", resp)

# print("successfully created basketball point", stats_client.SetBasketballPoint(basketball_pb2.SetBasketballPointRequest(
#     eventId=str(resp.eventId), 
#     player="joe", 
#     assist="biden", 
#     result="made", 
#     point="1"
# )))

# print("query field goal percentage", stats_client.GetFieldGoalPercentage(basketball_pb2.GetFieldGoalPercentageRequest(
#     gameId="b42f749b-4501-481b-82d8-7c9fadb1bd38",
# )))

# print("query three point percentage", stats_client.GetThreePointPercentage(basketball_pb2.GetThreePointPercentageRequest(
#     gameId="b42f749b-4501-481b-82d8-7c9fadb1bd38",
# )))

# print("query free throws made", stats_client.GetFreeThrowsMade(basketball_pb2.GetFreeThrowsMadeRequest(
#     gameId="b42f749b-4501-481b-82d8-7c9fadb1bd38",
# )))

# print("query total turnovers by team", stats_client.GetTotalTurnoversByTeam(basketball_pb2.GetTotalTurnoversByTeamRequest(
#     gameId="b42f749b-4501-481b-82d8-7c9fadb1bd38",
# )))

# print("query total steals by team", stats_client.GetTotalStealsByTeam(basketball_pb2.GetTotalStealsByTeamRequest(
#     gameId="b42f749b-4501-481b-82d8-7c9fadb1bd38",
# )))

print("Get Top Five players by Points Per Game", stats_client.GetTopFivePlayersByPointsPerGame(basketball_pb2.GetTopFivePlayersByPointsPerGameRequest(
    leagueId="890efb7f-a729-4c81-9b67-4b1d605a99ba",
)))