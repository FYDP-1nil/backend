# stats service
from concurrent import futures
import logging
from turtle import home

import grpc
import stats_pb2
import stats_pb2_grpc
import psycopg2 as pg

# cursor to execute DB statements
conn = None
class Stats(stats_pb2_grpc.StatsServicer):

    def CreateGame(self, request, context):
        cur = conn.cursor()
        cur.execute("INSERT INTO soccergames (home, away) VALUES (%s, %s) RETURNING id;", (request.homeTeam, request.awayTeam))
        gameId = cur.fetchone()[0]
        print(gameId)
        conn.commit()

        return stats_pb2.CreateGameResponse(gameId=gameId)

    def GetShots(self, request, context):
        cur = conn.cursor() 
        gameId = request.gameId
        
        # get home team and away team
        cur.execute("SELECT home, away FROM soccergames WHERE id = %s", gameId)
        homeTeam, awayTeam = cur.fetchone()
        resp = stats_pb2.GetShotsResponse()

        # get home team shots
        cur.execute("SELECT IsGoal, IsOnTarget, Player, Assist, soccershotime FROM soccershots WHERE TeamFor = %s AND GameId = %s;", homeTeam, gameId)
        homeTeamShots = []
        for s in cur.fetchall(): 
            shot = stats_pb2.Shot(
                isGoal= s[0],
                isOnTarget = s[1],
                scorer = s[2], 
                assist = s[3], 
                time = s[4]
            )
            homeTeamShots.append(shot)
        resp.teamFor = homeTeamShots

        # get away team shots
        cur.execute("SELECT IsGoal, IsOnTarget, Player, Assist, soccershotime FROM soccershots WHERE TeamFor = %s AND GameId = %s;", awayTeam, gameId)
        awayTeamShots = []
        for s in cur.fetchall(): 
            shot = stats_pb2.Shot(
                isGoal= s[0],
                isOnTarget = s[1],
                scorer = s[2], 
                assist = s[3], 
                time = s[4]
            )
            awayTeamShots.append(shot)
        resp.teamAgainst = awayTeamShots
        
        return resp

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
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    stats_pb2_grpc.add_StatsServicer_to_server(Stats(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    logger.debug("listening on port 50052")

    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger("stats")
    setupDb()
    serve(logger)
