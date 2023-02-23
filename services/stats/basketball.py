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


        