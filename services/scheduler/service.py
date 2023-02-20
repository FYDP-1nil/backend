# stats service
from concurrent import futures
import logging
from sre_constants import SUCCESS
# import uuid

import grpc
from ..gen import stats_pb2
from ..gen import stats_pb2_grpc
import psycopg2 as pg

# cursor to execute DB statements
conn = None

# def setupDb(): 
#     global conn
#     conn = pg.connect("dbname=postgres user=postgres password=very_secret_db_password host=1nil-db")

def serve(logger):
    # setupDb()
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # stats_pb2_grpc.add_StatsServicer_to_server(Stats(), server)
    server.add_insecure_port('[::]:50053')
    server.start()
    logger.debug("listening on port 50053")

    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger("scheduler")
    # setupDb()
    serve(logger)
