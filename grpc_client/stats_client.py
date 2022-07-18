import os
import grpc

import stats_pb2 
from stats_pb2_grpc import StatsStub

host = os.getenv("GRPC_HOST", "localhost")
channel = grpc.insecure_channel(f"{host}:50052")
stats_client = StatsStub(channel)

res = stats_client.CreateGame(stats_pb2.CreateGameRequest(homeTeam="test", awayTeam="test2", userId="test3"))
print("this is comiung from db: ", res)
