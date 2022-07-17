# stats service
from concurrent import futures
import logging

import grpc
import stats_pb2
import stats_pb2_grpc


class Stats(stats_pb2_grpc.StatsServicer):

    def CreateGame(self, request, context):
        # TODO - implement
        return stats_pb2.CreateGameResponse(gameId="this-is-a-test-gameId")


def serve(logger):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    stats_pb2_grpc.add_StatsServicer_to_server(Stats(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    logger.debug("listening on port 50052")

    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger("stats")
    serve(logger)
