from ..gen import basketball_pb2
from ..gen import stats_pb2


class Gridiron():
    def __init__(self, conn):
        self.conn = conn

    def CreateGridironGame(self, request):
        cur = self.conn.cursor()
        cur.execute("INSERT INTO gridirongames (leagueId, home, away) VALUES (%s, %s, %s) RETURNING id;",
                    (request.leagueId, request.homeTeam, request.awayTeam))
        gameId = cur.fetchone()[0]
        print(gameId)
        self.conn.commit()

        return gameId

    def SetGridironEvent(self, request):
        cur = self.conn.cursor()
        cur.execute(
            "INSERT INTO gridirongameevents (gameId, playType, period, teamFor, teamAgainst) VALUES (%s, %s, %s, %s, %s) " +
            "RETURNING id;", (request.gameId, request.playType, request.period, request.teamFor, request.teamAgainst))
        eventId = cur.fetchone()[0]
        print(eventId)
        self.conn.commit()

        return eventId

