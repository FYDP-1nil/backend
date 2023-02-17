import os
import grpc

host = os.getenv("STREAMER_GRPC_HOST", "localhost")
channel = grpc.insecure_channel(f"{host}:50051")
