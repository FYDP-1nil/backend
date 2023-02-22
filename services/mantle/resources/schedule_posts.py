from flask import request
from flask_restful import Resource
from backend.services.mantle.channels.scheduler_channel import channel
from backend.services.gen.scheduler_pb2_grpc import SchedulerStub
from backend.services.gen.scheduler_pb2 import SetPostRequest
from flask_jwt_extended import jwt_required

scheduler_client = SchedulerStub(channel)


class SchedulePost(Resource):

    @classmethod
    @jwt_required()
    def post(cls):
        json_data = request.get_json()
        post_text = json_data.get("post_text")
        scheduler_request = SetPostRequest(postMessage=post_text)
        scheduler_response = scheduler_client.SetPost(
            scheduler_request
        )
        if scheduler_response.success:
            return_msg = "Successfully posted on Facebook."
            return {"post_status": return_msg}, 200
        else:
            return_msg = "There was an error in posting to Facebook. Please try again."
            return {"post_status": return_msg}, 400
