import os
import grpc

host = os.getenv("GRPC_HOST", "localhost")
channel = grpc.insecure_channel(f"{host}:50051")
