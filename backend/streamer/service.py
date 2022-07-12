# streamer service
from concurrent import futures
import logging

import grpc
import streamer_pb2
import streamer_pb2_grpc


class Streamer(streamer_pb2_grpc.StreamerServicer):

    def ObtainTwitchKey(self, request, context):
        # TODO: implement
        return streamer_pb2.ObtainTwitchKeyResponse(key="")

    def ObtainYoutubeKey(self, request, context):
        # TODO: implement
        return streamer_pb2.ObtainYoutubeKeyResponse(key="")


def serve(logger):
    
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    streamer_pb2_grpc.add_StreamerServicer_to_server(Streamer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    logger.debug("listening on port 500051")
    
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig(level = logging.DEBUG)
    logger = logging.getLogger("streamer")
    serve(logger)
