from ..gen import basketball_pb2
from ..gen import stats_pb2

class Basketball(): 
    def __init__(self, conn): 
        self.conn = conn

    def CreateBasketballGame(self, request):         
        cur = self.conn.cursor() 
        cur.execute("INSERT INTO basketballgames (leagueId, home, away) VALUES (%s, %s, %s) RETURNING id;", (request.leagueId, request.homeTeam, request.awayTeam))
        gameId = cur.fetchone()[0]
        print(gameId)
        self.conn.commit()

        return gameId

    def SetBasketballEvent(self, request): 
        cur = self.conn.cursor()
        cur.execute("INSERT INTO basketballgameevents (gameId, playType, period, teamFor, teamAgainst) VALUES (%s, %s, %s, %s, %s) " + 
                    "RETURNING id;", (request.gameId, request.playType, request.period, request.teamFor, request.teamAgainst))
        eventId = cur.fetchone()[0]
        print(eventId)
        self.conn.commit()

        return eventId

    def SetBasketballPoint(self, request): 
        cur = self.conn.cursor()
        cur.execute("INSERT INTO basketballpoints (eventId, player, assist, result, point) VALUES (%s, %s, %s, %s, %s) " + 
                    "RETURNING id;", (request.eventId, request.player, request.assist, request.result, request.point))
        pointId = cur.fetchone()[0]
        print(pointId)
        self.conn.commit()

        return True

    def SetBasketballSteal(self, request): 
        cur = self.conn.cursor()
        cur.execute("INSERT INTO basketballsteals (eventId, player) VALUES (%s, %s) " + 
                    "RETURNING id;", (request.eventId, request.player))
        stealId = cur.fetchone()[0]
        print(stealId)
        self.conn.commit()

        return True
    
    def SetBasketballBlock(self, request): 
        cur = self.conn.cursor()
        cur.execute("INSERT INTO basketballblocks (eventId, player) VALUES (%s, %s) " + 
                    "RETURNING id;", (request.eventId, request.player))
        id = cur.fetchone()[0]
        print(id)
        self.conn.commit()

        return True
    
    def SetBasketballFoul(self, request): 
        cur = self.conn.cursor()
        cur.execute("INSERT INTO basketballfouls (eventId, player, reason) VALUES (%s, %s, %s) " + 
                    "RETURNING id;", (request.eventId, request.player, request.reason))
        id = cur.fetchone()[0]
        print(id)
        self.conn.commit()

        return True

    def SetBasketballTurnover(self, request): 
        cur = self.conn.cursor()
        cur.execute("INSERT INTO basketballturnovers (eventId, player) VALUES (%s, %s) " + 
                    "RETURNING id;", (request.eventId, request.player))
        id = cur.fetchone()[0]
        print(id)
        self.conn.commit()

        return True

    def SetBasketballRebound(self, request): 
        cur = self.conn.cursor()
        cur.execute("INSERT INTO basketballrebounds (eventId, player) VALUES (%s, %s) " + 
                    "RETURNING id;", (request.eventId, request.player))
        id = cur.fetchone()[0]
        print(id)
        self.conn.commit()

        return True

    def SetBasketballGameEnd(self, request): 
        cur = self.conn.cursor()
        cur.execute("INSERT INTO basketballgameends (eventId, ptsHome, ptsAway) VALUES (%s, %s, %s) " + 
                    "RETURNING id;", (request.eventId, request.ptsHome, request.ptsAway))
        id = cur.fetchone()[0]
        print(id)
        self.conn.commit()

        return True
        