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
        print("inserting bb point")
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
        
    def GetFieldGoalPercentage(self, request): 
        cur = self.conn.cursor()
        gameId = str(request.gameId)
        qry = f"""
                    WITH home_fgp AS (
                        SELECT g.home, ROUND(COUNT(CASE WHEN p.result = 'made' then 1 else NULL end)::numeric / COUNT(p.id), 2) AS fgp
                        FROM basketballpoints p
                        INNER JOIN basketballgameevents e ON e.id = p.eventId
                        INNER JOIN basketballgames g ON e.gameId = g.id
                        WHERE e.teamFor = g.home AND g.id = '{gameId}'
                        GROUP BY g.home
                    ), away_fgp AS (
                        SELECT g.away, ROUND(COUNT(CASE WHEN p.result = 'made' then 1 else NULL end)::numeric / COUNT(p.id), 2) AS fgp
                        FROM basketballpoints p
                        INNER JOIN basketballgameevents e ON e.id = p.eventId
                        INNER JOIN basketballgames g ON e.gameId = g.id
                        WHERE e.teamFor = g.away AND g.id = '{gameId}'
                        GROUP BY g.away
                    )
                    SELECT COALESCE((SELECT fgp FROM home_fgp), 0) AS field_goal_percentage
                    UNION ALL
                    SELECT COALESCE((SELECT fgp from away_fgp), 0) AS field_goal_percentage;
                """
        cur.execute(qry)
        output = cur.fetchall()
        teamForStat = output[0][0]
        teamAgainstStat = output[1][0]
        print("GetFieldGoalPercentage query result => ", (teamForStat, teamAgainstStat))
        return (teamForStat, teamAgainstStat)
        
    def GetThreePointPercentage(self, request): 
        cur = self.conn.cursor()
        gameId = str(request.gameId)
        qry = f"""
                    WITH home_3pt_pct AS (
                        SELECT ROUND(COUNT(CASE WHEN p.result = 'made' then 1 else NULL end)::numeric / COUNT(p.id), 2) AS three_points_pct
                        FROM basketballpoints p
                        INNER JOIN basketballgameevents e ON p.eventId = e.id
                        INNER JOIN basketballgames g ON e.gameId = g.id
                        WHERE p.point = 3 AND e.teamFor = g.home AND g.id = '{gameId}'
                        GROUP BY g.home
                    ), away_3pt_pct AS (
                        SELECT ROUND(COUNT(CASE WHEN p.result = 'made' then 1 else NULL end)::numeric / COUNT(p.id), 2) AS three_points_pct
                        FROM basketballpoints p
                        INNER JOIN basketballgameevents e ON p.eventId = e.id
                        INNER JOIN basketballgames g ON e.gameId = g.id
                        WHERE p.point = 3 AND e.teamFor = g.away AND g.id = '{gameId}'
                        GROUP BY g.away
                    )
                    SELECT COALESCE((SELECT three_points_pct FROM home_3pt_pct), 0) AS three_points_percentage
                    UNION ALL
                    SELECT COALESCE((SELECT three_points_pct FROM away_3pt_pct), 0) AS three_points_percentage;
                """
        cur.execute(qry)
        output = cur.fetchall()
        teamForStat = output[0][0]
        teamAgainstStat = output[1][0]
        print("GetThreePointPercentage query result => ", (teamForStat, teamAgainstStat))
        return (teamForStat, teamAgainstStat)
        
    def GetFreeThrowsMade(self, request): 
        cur = self.conn.cursor()
        gameId = str(request.gameId)
        qry = f"""
                    WITH home_free_throw_pct AS (
                        SELECT ROUND(COUNT(CASE WHEN p.result = 'made' then 1 else NULL end)::numeric / COUNT(p.id), 2) AS free_throw_pct
                        FROM basketballpoints p
                        INNER JOIN basketballgameevents e ON p.eventId = e.id
                        INNER JOIN basketballgames g ON e.gameId = g.id
                        WHERE p.point = 1 AND e.teamFor = g.home AND g.id = '{gameId}'
                        GROUP BY g.home
                    ), away_free_throw_pct AS (
                        SELECT ROUND(COUNT(CASE WHEN p.result = 'made' then 1 else NULL end)::numeric / COUNT(p.id), 2) AS free_throw_pct
                        FROM basketballpoints p
                        INNER JOIN basketballgameevents e ON p.eventId = e.id
                        INNER JOIN basketballgames g ON e.gameId = g.id
                        WHERE p.point = 1 AND e.teamFor = g.away AND g.id = '{gameId}'
                        GROUP BY g.away
                    )
                    SELECT COALESCE((SELECT free_throw_pct FROM home_free_throw_pct), 0) AS free_throw_percentage
                    UNION ALL
                    SELECT COALESCE((SELECT free_throw_pct FROM away_free_throw_pct), 0) AS free_throw_percentage;
                """
        cur.execute(qry)
        output = cur.fetchall()
        teamForStat = output[0][0]
        teamAgainstStat = output[1][0]
        print("GetFreeThrowsMade query result => ", (teamForStat, teamAgainstStat))
        return (teamForStat, teamAgainstStat)
        
    def GetTotalTurnoversByTeam(self, request): 
        cur = self.conn.cursor()
        gameId = str(request.gameId)
        qry = f"""
                    WITH home_turnovers AS (
                        SELECT COUNT(t.id) AS turnovers
                        FROM basketballturnovers t
                        INNER JOIN basketballgameevents e ON t.eventId = e.id
                        INNER JOIN basketballgames g ON e.gameId = g.id
                        WHERE e.teamFor = g.home AND g.id = '{gameId}'
                        GROUP BY g.home
                    ), away_turnovers AS (
                        SELECT COUNT(t.id) AS turnovers
                        FROM basketballturnovers t
                        INNER JOIN basketballgameevents e ON t.eventId = e.id
                        INNER JOIN basketballgames g ON e.gameId = g.id
                        WHERE e.teamFor = g.away AND g.id = '{gameId}'
                        GROUP BY g.away
                    )
                    SELECT COALESCE((SELECT * FROM home_turnovers), 0) AS turnovers
                    UNION ALL
                    SELECT COALESCE((SELECT * FROM away_turnovers), 0) AS turnovers;
                """
        cur.execute(qry)
        output = cur.fetchall()
        teamForStat = output[0][0]
        teamAgainstStat = output[1][0]
        print("GetTotalTurnoversByTeam query result => ", (teamForStat, teamAgainstStat))
        return (teamForStat, teamAgainstStat)
        
    def GetTotalStealsByTeam(self, request): 
        cur = self.conn.cursor()
        gameId = str(request.gameId)
        qry = f"""
                    WITH home_steals AS (
                        SELECT COUNT(s.id) AS steals
                        FROM basketballsteals s
                        INNER JOIN basketballgameevents e ON s.eventId = e.id
                        INNER JOIN basketballgames g ON e.gameId = g.id
                        WHERE e.teamFor = g.home AND g.id = '{gameId}'
                        GROUP BY g.home
                    ), away_steals AS (
                        SELECT COUNT(s.id) AS steals
                        FROM basketballsteals s
                        INNER JOIN basketballgameevents e ON s.eventId = e.id
                        INNER JOIN basketballgames g ON e.gameId = g.id
                        WHERE e.teamFor = g.away AND g.id = '{gameId}'
                        GROUP BY g.away
                    )
                    SELECT COALESCE((SELECT * FROM home_steals), 0) AS steals
                    UNION ALL
                    SELECT COALESCE((SELECT * FROM away_steals), 0) AS steals;
                """
        cur.execute(qry)
        output = cur.fetchall()
        teamForStat = output[0][0]
        teamAgainstStat = output[1][0]
        print("GetTotalStealsByTeam query result => ", (teamForStat, teamAgainstStat))
        return (teamForStat, teamAgainstStat)