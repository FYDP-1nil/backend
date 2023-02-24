# stats service
from concurrent import futures
import logging
from sre_constants import SUCCESS
import uuid

import grpc
from ..gen import stats_pb2
from ..gen import stats_pb2_grpc
import psycopg2 as pg
import psycopg2.extras

# cursor to execute DB statements
conn = None
# register uuid type
psycopg2.extras.register_uuid()

class Stats(stats_pb2_grpc.StatsServicer):

    def CreateGame(self, request, context):
        cur = conn.cursor()
        league_id = uuid.UUID(request.leagueId)
        print(league_id)
        cur.execute("INSERT INTO soccergames (leagueId, home, away) VALUES (%s, %s, %s) RETURNING id;", (league_id, request.homeTeam, request.awayTeam))
        gameId = str(cur.fetchone()[0])
        conn.commit()

        return stats_pb2.CreateGameResponse(gameId=gameId)

    def GetShots(self, request, context):
        cur = conn.cursor() 
        gameId = request.gameId
        
        # get home team and away team
        print(gameId)
        cur.execute("SELECT home, away FROM soccergames WHERE id = %s;", (gameId, ))
        homeTeam, awayTeam = cur.fetchone()
        print("these are the teams involved", homeTeam, awayTeam)
        resp = stats_pb2.GetShotsResponse()

        # get home team shots
        cur.execute("SELECT IsGoal, IsOnTarget, Player, Assist, soccershottime FROM soccershots WHERE TeamFor = %s AND GameId = %s;", (homeTeam, gameId))
        homeTeamShots = []
        temp = cur.fetchall()
        print("home shots: ", temp)
        for s in temp: 
            shot = stats_pb2.Shot(
                isGoal= s[0],
                isOnTarget = s[1],
                scorer = s[2], 
                assist = s[3], 
                time = s[4]
            )
            homeTeamShots.append(shot)
        resp.teamFor.extend(homeTeamShots)

        # get away team shots
        cur.execute("SELECT IsGoal, IsOnTarget, Player, Assist, soccershottime FROM soccershots WHERE TeamFor = %s AND GameId = %s;", (awayTeam, gameId))
        awayTeamShots = []
        temp = cur.fetchall()
        print("away shots: ", temp)
        for s in temp: 
            shot = stats_pb2.Shot(
                isGoal= s[0],
                isOnTarget = s[1],
                scorer = s[2], 
                assist = s[3], 
                time = s[4]
            )
            awayTeamShots.append(shot)
        resp.teamAgainst.extend(awayTeamShots)
        
        return resp

    def GetFouls(self, request, context):
        cur = conn.cursor() 
        gameId = request.gameId
        
        # get home team and away team
        cur.execute("SELECT home, away FROM soccergames WHERE id = %s;", (gameId, ))
        homeTeam, awayTeam = cur.fetchone()
        print("these are the teams involved", homeTeam, awayTeam)
        resp = stats_pb2.GetFoulsResponse()

        # get home team shots
        cur.execute("SELECT IsYellow, IsRed, Player, Reason, soccerfoultime FROM soccerfouls WHERE TeamFor = %s AND GameId = %s;", (homeTeam, gameId))
        homeTeamFouls = []
        temp = cur.fetchall()
        print("home fouls: ", temp)
        for f in temp: 
            foul = stats_pb2.Foul(
                isYellow = f[0],
                isRed = f[1],
                player = f[2], 
                reason = f[3],
                time = f[4]
            )
            homeTeamFouls.append(foul)
        resp.teamFor.extend(homeTeamFouls)

        # get away team shots
        cur.execute("SELECT IsYellow, IsRed, Player, Reason, soccerfoultime FROM soccerfouls WHERE TeamFor = %s AND GameId = %s;", (awayTeam, gameId))
        awayTeamFouls = []
        temp = cur.fetchall()
        print("away fouls: ", temp)
        for f in temp: 
            foul = stats_pb2.Foul(
                isYellow = f[0],
                isRed = f[1],
                player = f[2], 
                reason = f[3],
                time = f[4]
            )
            awayTeamFouls.append(foul)
        resp.teamAgainst.extend(awayTeamFouls)
        
        return resp

    def GetOffsides(self, request, context):
        cur = conn.cursor() 
        gameId = request.gameId
        
        # get home team and away team
        cur.execute("SELECT home, away FROM soccergames WHERE id = %s;", (gameId, ))
        homeTeam, awayTeam = cur.fetchone()
        print("these are the teams involved", homeTeam, awayTeam)
        resp = stats_pb2.GetOffsidesResponse()

        # get home team shots
        cur.execute("SELECT offsidetime FROM socceroffsides WHERE TeamFor = %s AND GameId = %s;", (homeTeam, gameId))
        homeTeamOffsides = []
        temp = cur.fetchall()
        print("home offsides: ", temp)
        for o in temp: 
            offside = stats_pb2.Offside(
                time=o[0]
            )
            homeTeamOffsides.append(offside)
        resp.teamFor.extend(homeTeamOffsides)

        # get away team shots
        cur.execute("SELECT offsidetime FROM socceroffsides WHERE TeamFor = %s AND GameId = %s;", (awayTeam, gameId))
        awayTeamOffsides = []
        temp = cur.fetchall()
        print("away offsides: ", temp)
        for o in temp: 
            offside = stats_pb2.Offside(
                time = o[0]
            )
            awayTeamOffsides.append(offside)
        resp.teamAgainst.extend(awayTeamOffsides)
        
        return resp

    def SetShot(self, request, context): 
        cur = conn.cursor() 
        cur.execute("INSERT INTO soccershots (GameId, TeamFor, TeamAgainst, IsGoal, IsOnTarget, Player, Assist, soccershottime) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (request.gameId, request.teamFor, request.teamAgainst, request.shotDetails.isGoal, request.shotDetails.isOnTarget, request.shotDetails.scorer, request.shotDetails.assist, request.shotDetails.time))
        conn.commit() 

        return stats_pb2.SetShotResponse(success=True)

    def SetFoul(self, request, context):
        cur = conn.cursor() 
        cur.execute("INSERT INTO soccerfouls (GameId, TeamFor, TeamAgainst, Player, Reason, IsYellow, IsRed, soccerfoultime) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (request.gameId, request.teamFor, request.teamAgainst, request.foulDetails.player, request.foulDetails.reason, request.foulDetails.isYellow, request.foulDetails.isRed, request.foulDetails.time))
        conn.commit() 

        return stats_pb2.SetShotResponse(success=True)

    def SetOffside(self, request, context):
        cur = conn.cursor() 
        cur.execute("INSERT INTO socceroffsides (GameId, TeamFor, TeamAgainst, offsidetime) VALUES (%s, %s, %s, %s)", (request.gameId, request.teamFor, request.teamAgainst, request.offsideDetails.time))
        conn.commit() 

        return stats_pb2.SetOffsideResponse(success=True)

    def SetEvent(self, request, context):
        cur = conn.cursor()
        game_id = uuid.UUID(request.gameId)
        cur.execute("INSERT INTO soccerevents (EventType, GameId, SocEvent) VALUES (%s, %s, %s);", (request.eventType, game_id, request.event))
        conn.commit() 

        return stats_pb2.SetEventResponse(success=True)


def setupDb(): 
    global conn
    conn = pg.connect("dbname=postgres user=postgres password=very_secret_db_password host=1nil-db")

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
    setupDb()
    serve(logger)
