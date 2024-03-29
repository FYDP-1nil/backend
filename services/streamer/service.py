# streamer service
from concurrent import futures
import logging
import requests

import grpc
from ..gen import streamer_pb2
from ..gen import streamer_pb2_grpc

class Streamer(streamer_pb2_grpc.StreamerServicer):

    def ObtainTwitchKey(self, request, context):
        stream_key = get_twitch_stream_key()
        return streamer_pb2.ObtainTwitchKeyResponse(key=stream_key)

    def ObtainYoutubeKey(self, request, context):
        # TODO: implement
        return streamer_pb2.ObtainYoutubeKeyResponse(key="")

def get_twitch_stream_key():

    oauth = 'hwlx7ujsduz9x75i75v8malkhzhrc2'

    headers = {
        'Authorization': 'Bearer ' + oauth
    }

    response = requests.get('https://id.twitch.tv/oauth2/validate', headers=headers).json()
    client_id = response['client_id']
    broadcaster_id = response['user_id']
    headers = {
        'Authorization': 'Bearer ' + oauth,
        'Client-Id': client_id
    }
    stream_key = requests.get('https://api.twitch.tv/helix/streams/key',
                              params={'broadcaster_id': broadcaster_id},
                              headers=headers).json()
    return stream_key.get("data", {})[0].get("stream_key", "")

def serve(logger):
    
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    streamer_pb2_grpc.add_StreamerServicer_to_server(Streamer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    logger.debug("listening on port 50051")
    
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig(level = logging.DEBUG)
    logger = logging.getLogger("streamer")
    serve(logger)
