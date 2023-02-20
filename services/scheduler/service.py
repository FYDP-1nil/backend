# stats service
from concurrent import futures
import logging
import grpc
from ..gen import scheduler_pb2
from ..gen import scheduler_pb2_grpc
class Scheduler(scheduler_pb2_grpc.SchedulerServicer):

    def SetPost(self, request, context):
        resp = schedule_post()
        return scheduler_pb2.SetPostResponse(success=resp)

def schedule_post():
    pass

def serve(logger):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    scheduler_pb2_grpc.add_SchedulerServicer_to_server(Scheduler(), server)
    server.add_insecure_port('[::]:50053')
    server.start()
    logger.debug("listening on port 50053")

    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger("scheduler")
    serve(logger)
