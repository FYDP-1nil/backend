# streamer service
from concurrent import futures
import logging
import requests

import grpc
import streamer_pb2
import streamer_pb2_grpc


class Streamer(streamer_pb2_grpc.StreamerServicer):

    def ObtainTwitchKey(self, request, context):
        stream_key = get_twitch_stream_key()
        return streamer_pb2.ObtainTwitchKeyResponse(key=stream_key)

    def ObtainYoutubeKey(self, request, context):
        # TODO: implement
        return streamer_pb2.ObtainYoutubeKeyResponse(key="")


def serve(logger):
    
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    streamer_pb2_grpc.add_StreamerServicer_to_server(Streamer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    logger.debug("listening on port 50051")
    
    server.wait_for_termination()

def get_twitch_stream_key():

    # TODO - get oauth dynamically
    oauth = '1086qrtpttkoegzh1y638n8tdxiud2'

    headers = {
        'Authorization': 'Bearer ' + oauth
    }

    client_id = requests.get('https://id.twitch.tv/oauth2/validate', headers=headers).json()['client_id']
    id = requests.get('https://id.twitch.tv/oauth2/validate', headers=headers).json()['user_id']
    headers = {
        'Authorization': 'Bearer ' + oauth,
        'Client-Id': client_id
    }
    stream_key = requests.get('https://api.twitch.tv/helix/streams/key',
                              params={'broadcaster_id': id},
                              headers=headers).json()
    return stream_key.get("data", {})[0].get("stream_key", "")

if __name__ == '__main__':
    logging.basicConfig(level = logging.DEBUG)
    logger = logging.getLogger("streamer")
    serve(logger)
