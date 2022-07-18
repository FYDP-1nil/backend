# stats service
from concurrent import futures
import logging

import grpc
import stats_pb2
import stats_pb2_grpc
import psycopg2 as pg

# cursor to execute DB statements
conn = None
class Stats(stats_pb2_grpc.StatsServicer):

    def CreateGame(self, request, context):
        # TODO - implement
        cur = conn.cursor()
        cur.execute("INSERT INTO soccergames (home, away) VALUES (%s, %s) RETURNING id", (request.homeTeam, request.awayTeam))
        gameId = cur.fetchone()[0]
        # print(gameId)
        conn.commit()

        return stats_pb2.CreateGameResponse(gameId=gameId)

    def GetShots(self, request, context):
        # TODO - implement
        homeTeam = stats_pb2.GetShotsResponse()
        return stats_pb2.GetShotsResponse()

    def GetFouls(self, request, context):
        # TODO - implement
        pass

    def GetOffsides(self, request, context):
        # TODO - implement
        pass


def setupDb(): 
    global conn
    conn = pg.connect("dbname=1nil user=postgres")

def serve(logger):
    setupDb()
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
