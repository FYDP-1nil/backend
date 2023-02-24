# stats service
from concurrent import futures
import logging
import grpc
import requests
from ..gen import scheduler_pb2
from ..gen import scheduler_pb2_grpc
class Scheduler(scheduler_pb2_grpc.SchedulerServicer):

    def SetPost(self, request, context):
        resp = schedule_post(request.postMessage)
        return scheduler_pb2.SetPostResponse(success=resp)

def schedule_post(post_text):
    page_id_1 = 101787976183954
    facebook_access_token_1 = 'EAAILuM32DZBEBANiH9IUe3hRNeNupYikcYJbq2qZBXx1I1ZBx3bweC2imZAy79Y3t8bNwjWCKuTMafZAeTO22mRP7vaFJxNaItPlTWEsZBqw0QEb2CNdISEO42i1xWa6YedJpHF8c8Pf37RqvGAUZB6c7f3kZA3uKeQixQ0GN7p7f208uDNzZAsQfSZBsA9ENIGNT6ftYuk3hp5gZDZD'
    post_url = 'https://graph.facebook.com/{}/feed/'.format(page_id_1)
    payload = {
        'message': post_text,
        'access_token': facebook_access_token_1
    }
    r = requests.post(post_url, payload)
    return r.status_code == 200

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
