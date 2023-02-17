from flask_restful import Resource
from backend.services.mantle.channels.streamer_channel import channel
from backend.services.gen.streamer_pb2_grpc import StreamerStub
from backend.services.gen.streamer_pb2 import ObtainTwitchKeyRequest, ObtainYoutubeKeyRequest
from flask_jwt_extended import jwt_required

INVALID_STREAM_TYPE = "Invalid stream type"

streamer_client = StreamerStub(channel)


class Stream(Resource):

    @classmethod
    @jwt_required()
    def get(cls, stream_type: str):
        if stream_type not in ("youtube", "twitch"):
            return {"message": INVALID_STREAM_TYPE}, 404

        # TODO - in the future, pass in user_id or something for dynamic
        # TODO - generation of the Oauth token
        if stream_type == "twitch":
            streamer_request = ObtainTwitchKeyRequest(user="test")
            streamer_response = streamer_client.ObtainTwitchKey(
                streamer_request
            )
        else:
            streamer_request = ObtainYoutubeKeyRequest(user="test")
            streamer_response = streamer_client.ObtainYoutubeKey(
                streamer_request
            )
        stream_key = streamer_response.key
        return {"stream_key": stream_key}, 200
