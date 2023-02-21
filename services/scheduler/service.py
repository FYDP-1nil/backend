# stats service
from concurrent import futures
import logging
import grpc
import requests
from ..gen import scheduler_pb2
from ..gen import scheduler_pb2_grpc
class Scheduler(scheduler_pb2_grpc.SchedulerServicer):

    def SetPost(self, request, context):
        # send ret message recv from mantle
        dummy_text_from_mantle = "Hi I am 1nil scheduler guys! Hope you like me"
        resp = schedule_post(dummy_text_from_mantle)
        return scheduler_pb2.SetPostResponse(success=resp)

def schedule_post(post_text):
    page_id_1 = 101787976183954
    facebook_access_token_1 = 'EAAILuM32DZBEBAEzXmfQKvjHyBcsYum2kiWOn7yAxcTxtSHKvJHfreIVGThZByL03p7Qw2IBG3ZCcZA6LIoXdgLaHRf41XMB5J0UCQfZCMwWDm8lJs9YBalq5HnsWZBLIHRfLtALZCmeBJDVU6DUSZAQnY4633H247bTrTidwyS1ORZCWBwzepnJoFYtrKFMcTET9NoZC7cvjwaKVp8BMRMk7PPeYIylZBogyc3rIyaazOjEAZDZD'
    post_url = 'https://graph.facebook.com/{}/feed/'.format(page_id_1)
    payload = {
        'message': post_text,
        'access_token': facebook_access_token_1
    }
    r = requests.post(post_url, payload)
    return (r.status_code == 200)

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