import os
import grpc

host = os.getenv("STATS_GRPC_HOST", "localhost")
channel = grpc.insecure_channel(f"{host}:50052")
