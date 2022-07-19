import os
import grpc

import stats_pb2 
from stats_pb2_grpc import StatsStub

host = os.getenv("GRPC_HOST", "localhost")
channel = grpc.insecure_channel(f"{host}:50052")
stats_client = StatsStub(channel)

# test createGame
res = stats_client.CreateGame(stats_pb2.CreateGameRequest(homeTeam="Chelsea", awayTeam="Madrid", userId="Zelek"))
print("this is comiung from db: ", res)
gameId = res.gameId

# test setShot 1 
print("test shot 1?: ", stats_client.SetShot(stats_pb2.SetShotRequest(
    gameId = gameId, 
    teamFor = "Chelsea",
    teamAgainst = "Madrid",
    shotDetails = stats_pb2.Shot(
        isGoal= True,
        isOnTarget = True, 
        scorer = "messi",
        assist = "ronald",
        time = 45 
    ) 
)))

# test setShot 2
print("test shot 2?: ", stats_client.SetShot(stats_pb2.SetShotRequest(
    gameId = gameId, 
    teamFor = "Madrid",
    teamAgainst = "Chelsea",
    shotDetails = stats_pb2.Shot(
        isGoal= True,
        isOnTarget = True, 
        scorer = "ronaldo",
        assist = "pele",
        time = 90
    ) 
)))

# test setShot 3
print("test shot 3?: ", stats_client.SetShot(stats_pb2.SetShotRequest(
    gameId = gameId, 
    teamFor = "Madrid",
    teamAgainst = "Chelsea",
    shotDetails = stats_pb2.Shot(
        isGoal= True,
        isOnTarget = True, 
        scorer = "asd",
        assist = "salah",
        time = 90
    ) 
)))

# test foul
print("test foul 1?: ", stats_client.SetFoul(stats_pb2.SetFoulRequest(
    gameId = gameId, 
    teamFor = "Madrid",
    teamAgainst = "Chelsea",
    foulDetails = stats_pb2.Foul(
        isYellow=True,
        isRed=True,
        player="Iram",
        reason="Shreyas"
    ) 
)))

# test foul 2
print("test foul 2?: ", stats_client.SetFoul(stats_pb2.SetFoulRequest(
    gameId = gameId, 
    teamFor = "Chelsea",
    teamAgainst = "Madrid",
    foulDetails = stats_pb2.Foul(
        isYellow=False,
        isRed=True,
        player="Banin",
        reason="madhur"
    ) 
)))

print("test offside: ", stats_client.SetOffside(stats_pb2.SetOffsideRequest(
    gameId = gameId, 
    teamFor = "Chelsea",
    teamAgainst = "Madrid",
    offsideDetails = stats_pb2.Offside(
        time=10
    ) 
)))

# test setEvent
print("test event: ", stats_client.SetEvent(stats_pb2.SetEventRequest(
    eventType = "testtype", 
    gameId = gameId,
    event = "json blob"
)))

# test getShots
resp = stats_client.GetShots(stats_pb2.GetShotsRequest(
    gameId = gameId
))

shotsFromHomeTeam = resp.teamFor
shotsFromAwayTeam = resp.teamAgainst
print("home team shots: ", shotsFromHomeTeam)
print("away team shots: ", shotsFromAwayTeam)

print("fouls", stats_client.GetFouls(stats_pb2.GetFoulsRequest(
    gameId=gameId
)))

print("offsides", stats_client.GetOffsides(stats_pb2.GetOffsidesRequest(
    gameId=gameId
)))