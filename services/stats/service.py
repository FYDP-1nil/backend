# stats service
from concurrent import futures
import logging
from sre_constants import SUCCESS
import uuid

import grpc
from ..gen import stats_pb2
from ..gen import stats_pb2_grpc
from ..gen import basketball_pb2
from ..gen import gridiron_pb2
import psycopg2 as pg
import psycopg2.extras
from .basketball import Basketball
from .gridiron import Gridiron
import sys


# cursor to execute DB statements
conn = None
# register uuid type
psycopg2.extras.register_uuid()

class Stats(stats_pb2_grpc.StatsServicer):

    def __init__(self, conn): 
        super().__init__()
        self.basketball_dal = Basketball(conn)
        self.gridiron_dal = Gridiron(conn)

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

    def SetEndGame(self, request, context):
        cur = conn.cursor()
        cur.execute("INSERT INTO soccergameends (GameId, goalsHome, goalsAway) VALUES (%s, %s, %s, %s)", (request.gameId, request.goalsHome, request.goalsAway))
        conn.commit()

        return stats_pb2.SetEndGameResponse(success=True)

    def SetEvent(self, request, context):
        cur = conn.cursor()
        game_id = uuid.UUID(request.gameId)
        cur.execute("INSERT INTO soccerevents (EventType, GameId, SocEvent) VALUES (%s, %s, %s);", (request.eventType, game_id, request.event))
        conn.commit()

        return stats_pb2.SetEventResponse(success=True)

    # Basketball operations
    
    # Write operations
    def CreateBasketballGame(self, request, context): 
        return basketball_pb2.CreateBasketballGameResponse(gameId=str(self.basketball_dal.CreateBasketballGame(request)))

    def SetBasketballEvent(self, request, context): 
        return basketball_pb2.SetBasketballEventResponse(eventId=str(self.basketball_dal.SetBasketballEvent(request)))

    def SetBasketballPoint(self, request, context): 
        return basketball_pb2.SetBasketballPointResponse(success=bool(self.basketball_dal.SetBasketballPoint(request)))

    def SetBasketballSteal(self, request, context): 
        return basketball_pb2.SetBasketballStealResponse(success=bool(self.basketball_dal.SetBasketballSteal(request)))

    def SetBasketballBlock(self, request, context): 
        return basketball_pb2.SetBasketballBlockResponse(success=bool(self.basketball_dal.SetBasketballBlock(request)))

    def SetBasketballFoul(self, request, context): 
        return basketball_pb2.SetBasketballFoulResponse(success=bool(self.basketball_dal.SetBasketballFoul(request)))

    def SetBasketballTurnover(self, request, context): 
        return basketball_pb2.SetBasketballTurnoverResponse(success=bool(self.basketball_dal.SetBasketballTurnover(request)))

    def SetBasketballGameEnd(self, request, context): 
        return basketball_pb2.SetBasketballGameEndResponse(success=bool(self.basketball_dal.SetBasketballGameEnd(request)))

    def SetBasketballRebound(self, request, context): 
        return basketball_pb2.SetBasketballReboundResponse(success=bool(self.basketball_dal.SetBasketballRebound(request)))

    # # Game-centric stats
    def GetFieldGoalPercentage(self, request, context):
        (teamForStat, teamAgainstStat) = self.basketball_dal.GetFieldGoalPercentage(request)
        return basketball_pb2.GetFieldGoalPercentageResponse(teamForStat=teamForStat, teamAgainstStat=teamAgainstStat)
    
    def GetThreePointPercentage(self, request, context):
        (teamForStat, teamAgainstStat) = self.basketball_dal.GetThreePointPercentage(request)
        return basketball_pb2.GetThreePointPercentageResponse(teamForStat=teamForStat, teamAgainstStat=teamAgainstStat)

    def GetFreeThrowsMade(self, request, context):
        (teamForStat, teamAgainstStat) = self.basketball_dal.GetFreeThrowsMade(request)
        return basketball_pb2.GetFreeThrowsMadeResponse(teamForStat=teamForStat, teamAgainstStat=teamAgainstStat)

    def GetTotalTurnoversByTeam(self, request, context):
        (teamForStat, teamAgainstStat) = self.basketball_dal.GetTotalTurnoversByTeam(request)
        return basketball_pb2.GetTotalTurnoversByTeamResponse(teamForStat=teamForStat, teamAgainstStat=teamAgainstStat)

    def GetTotalStealsByTeam(self, request, context):
        (teamForStat, teamAgainstStat) = self.basketball_dal.GetTotalStealsByTeam(request)
        return basketball_pb2.GetTotalStealsByTeamResponse(teamForStat=teamForStat, teamAgainstStat=teamAgainstStat)

    # # League-centric stats
    def GetTopFivePlayersByPointsPerGame(self, request, context):
        return basketball_pb2.GetTopFivePlayersByPointsPerGameResponse(resp=self.basketball_dal.GetTopFivePlayersByPointsPerGame(request))

    def GetTopFivePlayersByReboundsPerGame(self, request, context):
        return basketball_pb2.GetTopFivePlayersByReboundsPerGameResponse(resp=self.basketball_dal.GetTopFivePlayersByReboundsPerGame(request))
        
    def GetTopFivePlayersByAssistsPerGame(self, request, context):
        return basketball_pb2.GetTopFivePlayersByAssistsPerGameResponse(resp=self.basketball_dal.GetTopFivePlayersByAssistsPerGame(request))
        
    def GetTopFivePlayersByBlocksPerGame(self, request, context):
        return basketball_pb2.GetTopFivePlayersByBlocksPerGameResponse(resp=self.basketball_dal.GetTopFivePlayersByBlocksPerGame(request))
        
    def GetTopFivePlayersByStealsPerGame(self, request, context):
        return basketball_pb2.GetTopFivePlayersByStealsPerGameResponse(resp=self.basketball_dal.GetTopFivePlayersByStealsPerGame(request))
        
    def GetTopFivePlayersByFieldGoalPercentage(self, request, context):
        return basketball_pb2.GetTopFivePlayersByFieldGoalPercentageResponse(resp=self.basketball_dal.GetTopFivePlayersByFieldGoalPercentage(request))
        
    def GetTopFivePlayersBy3ptPercentage(self, request, context):
        return basketball_pb2.GetTopFivePlayersBy3ptPercentageResponse(resp=self.basketball_dal.GetTopFivePlayersBy3ptPercentage(request))
        
    def GetTopFivePlayersByFreeThrowPercentage(self, request, context):
        return basketball_pb2.GetTopFivePlayersByFreeThrowPercentageResponse(self.basketball_dal.GetTopFivePlayersByFreeThrowPercentage(request))

    # Gridiron Operations

    # Write operations 
    def CreateGridironGame(self, request, context):
        return gridiron_pb2.CreateGridironGameResponse(gameId=str(self.gridiron_dal.CreateGridironGame(request)))

    def SetGridironEvent(self, request, context): 
        return gridiron_pb2.SetGridironEventResponse(eventId=str(self.gridiron_dal.SetGridironEvent(request)))

    def SetGridironRush(self, request, context): 
        return gridiron_pb2.SetGridironRushResponse(success=bool(self.gridiron_dal.SetGridironRush(request)))

    def SetGridironThrow(self, request, context): 
        return gridiron_pb2.SetGridironThrowResponse(success=bool(self.gridiron_dal.SetGridironThrow(request)))

    def SetGridironKick(self, request, context): 
        return gridiron_pb2.SetGridironKickResponse(success=bool(self.gridiron_dal.SetGridironKick(request)))

    def SetGridironGameEnd(self, request, context): 
        return gridiron_pb2.SetGridironGameEndResponse(success=bool(self.gridiron_dal.SetGridironGameEnd(request)))

    # Game centric stats operations
    def GetTotalRushingYards(self, request, context): 
        (homeTeamResponse, awayTeamResponse) = self.gridiron_dal.GetTotalRushingYards(request)
        return gridiron_pb2.GetTotalRushingYardsResponse(homeTeamResponse=homeTeamResponse, awayTeamResponse=awayTeamResponse)

    def GetTotalPassingYards(self, request, context): 
        (homeTeamResponse, awayTeamResponse) = self.gridiron_dal.GetTotalPassingYards(request)
        return gridiron_pb2.GetTotalPassingYardsResponse(homeTeamResponse=homeTeamResponse, awayTeamResponse=awayTeamResponse)

    def GetAvgYardsPerPlay(self, request, context): 
        (homeTeamResponse, awayTeamResponse) = self.gridiron_dal.GetAvgYardsPerPlay(request)
        return gridiron_pb2.GetAvgYardsPerPlayResponse(homeTeamResponse=homeTeamResponse, awayTeamResponse=awayTeamResponse)

    def GetTotalTouchdowns(self, request, context): 
        (homeTeamResponse, awayTeamResponse) = self.gridiron_dal.GetTotalTouchdowns(request)
        return gridiron_pb2.GetTotalTouchdownsResponse(homeTeamResponse=homeTeamResponse, awayTeamResponse=awayTeamResponse)

    def GetTotalTurnovers(self, request, context): 
        (homeTeamResponse, awayTeamResponse) = self.gridiron_dal.GetTotalTurnovers(request)
        return gridiron_pb2.GetTotalTurnoversResponse(homeTeamResponse=homeTeamResponse, awayTeamResponse=awayTeamResponse)

    # League Centric stats operations
    def GetTopFivePlayersByRushingYards(self, request, context):
        return gridiron_pb2.GetTopFivePlayersByRushingYardsResponse(resp=self.gridiron_dal.GetTopFivePlayersByRushingYards(request))

    def GetTopFivePlayersByReceivingYards(self, request, context):
        return gridiron_pb2.GetTopFivePlayersByReceivingYardsResponse(resp=self.gridiron_dal.GetTopFivePlayersByReceivingYards(request))

    def GetTopFivePlayersByThrowingYards(self, request, context):
        return gridiron_pb2.GetTopFivePlayersByThrowingYardsResponse(resp=self.gridiron_dal.GetTopFivePlayersByThrowingYards(request))

    def GetTopFivePlayersByKicksMade(self, request, context):
        return gridiron_pb2.GetTopFivePlayersByKicksMadeResponse(resp=self.gridiron_dal.GetTopFivePlayersByKicksMade(request))

    def GetTopFivePlayersByCompletionPercentage(self, request, context):
        return gridiron_pb2.GetTopFivePlayersByCompletionPercentageResponse(resp=self.gridiron_dal.GetTopFivePlayersByCompletionPercentage(request))

    

def setupDb(): 
    global conn
    conn = pg.connect(f"dbname=postgres user=postgres password=very_secret_db_password host={sys.argv[1]}")

def serve(logger):
    setupDb()
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    stats_pb2_grpc.add_StatsServicer_to_server(Stats(conn), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    logger.debug("listening on port 50052")

    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger("stats")
    setupDb()
    serve(logger)
