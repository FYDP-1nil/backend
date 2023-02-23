import os
import grpc

host = os.getenv("SCHEDULER_GRPC_HOST", "localhost")
channel = grpc.insecure_channel(f"{host}:50053")
