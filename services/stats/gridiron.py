from ..gen import gridiron_pb2
from ..gen import stats_pb2

class Gridiron(): 
    def __init__(self, conn): 
        self.conn = conn

    def CreateGridironGame(self, request):         
        cur = self.conn.cursor() 
        cur.execute("INSERT INTO gridirongames (leagueId, home, away) VALUES (%s, %s, %s) RETURNING id;", (request.leagueId, request.homeTeam, request.awayTeam))
        gameId = cur.fetchone()[0]
        print(gameId)
        self.conn.commit()

        return gameId

    def SetGridironEvent(self, request): 
        cur = self.conn.cursor()
        cur.execute("INSERT INTO gridirongameevents (gameId, playType, period, teamFor, teamAgainst) VALUES (%s, %s, %s, %s, %s) " + 
                    "RETURNING id;", (request.gameId, request.playType, request.period, request.teamFor, request.teamAgainst))
        eventId = cur.fetchone()[0]
        print(eventId)
        self.conn.commit()

        return eventId

    def SetGridironRush(self, request): 
        cur = self.conn.cursor()
        cur.execute("INSERT INTO gridironrushes (eventId, player, yard, result) VALUES (%s, %s, %s, %s, %s) " + 
                    "RETURNING id;", (request.eventId, request.player, request.yard, request.result))
        rushId = cur.fetchone()[0]
        print(rushId)
        self.conn.commit()

        return True

    def SetGridironThrow(self, request): 
        cur = self.conn.cursor()
        cur.execute("INSERT INTO gridironthrows (eventId, playerThrowing, playerReceiving, yard, result) VALUES (%s, %s, %s, %s, %s) " + 
                    "RETURNING id;", (request.eventId, request.playerThrowing, request.playerReceiving, request.yard, request.result))
        throwId = cur.fetchone()[0]
        print(throwId)
        self.conn.commit()

        return True
    
    def SetGridironKick(self, request): 
        cur = self.conn.cursor()
        cur.execute("INSERT INTO gridironkicks (eventId, player, yard, result) VALUES (%s, %s, %s, %s) " + 
                    "RETURNING id;", (request.eventId, request.player, request.yard, request.result))
        id = cur.fetchone()[0]
        print(id)
        self.conn.commit()

        return True
    
    def SetGridironGameEnd(self, request): 
        cur = self.conn.cursor()
        cur.execute("INSERT INTO gridirongameends (eventId, ptsHome, ptsAway) VALUES (%s, %s, %s) " + 
                    "RETURNING id;", (request.eventId, request.ptsHome, request.ptsAway))
        id = cur.fetchone()[0]
        print(id)
        self.conn.commit()

        return True


        
    def GetTotalRushingYards(self, request): 
        cur = self.conn.cursor()
        gameId = str(request.gameId)
        qry = f"""
                    WITH home_rush_yards AS (
                        SELECT SUM(r.yard) AS rush_yards
                        FROM gridironrushes r
                        INNER JOIN gridirongameevents e ON r.eventId = e.id
                        INNER JOIN gridirongames g ON e.gameId = g.id
                        WHERE e.teamFor = g.home AND e.gameId = '{gameId}'
                        GROUP BY g.home
                    ), away_rush_yards AS (
                        SELECT SUM(r.yard) AS rush_yards
                        FROM gridironrushes r
                        INNER JOIN gridirongameevents e ON r.eventId = e.id
                        INNER JOIN gridirongames g ON e.gameId = g.id
                        WHERE e.teamFor = g.away AND e.gameId = '{gameId}'
                        GROUP BY g.away
                    )
                    SELECT COALESCE((SELECT * FROM home_rush_yards), 0) AS rush_yards
                    UNION ALL
                    SELECT COALESCE((SELECT * FROM away_rush_yards), 0) AS rush_yards;
                """
        cur.execute(qry)
        output = cur.fetchall()
        homeTeamResponse = output[0][0]
        awayTeamResponse = output[1][0]
        print("GetTotalRushingYards query result => ", (homeTeamResponse, awayTeamResponse))
        return (homeTeamResponse, awayTeamResponse)
        
    def GetTotalPassingYards(self, request): 
        cur = self.conn.cursor()
        gameId = str(request.gameId)
        qry = f"""
                    WITH home_pass_yards AS (
                        SELECT SUM(t.yard) AS pass_yards
                        FROM gridironthrows t
                        INNER JOIN gridirongameevents e ON t.eventId = e.id
                        INNER JOIN gridirongames g ON e.gameId = g.id
                        WHERE e.teamFor = g.home AND t.result != 'miss' AND e.gameId = '{gameId}'
                        GROUP BY g.home
                    ), away_pass_yards AS (
                        SELECT SUM(t.yard) AS pass_yards
                        FROM gridironthrows t
                        INNER JOIN gridirongameevents e ON t.eventId = e.id
                        INNER JOIN gridirongames g ON e.gameId = g.id
                        WHERE e.teamFor = g.away AND t.result != 'miss' AND e.gameId = '{gameId}'
                        GROUP BY g.away
                    )
                    SELECT COALESCE((SELECT * FROM home_pass_yards), 0) AS pass_yards
                    UNION ALL
                    SELECT COALESCE((SELECT * FROM away_pass_yards), 0) AS pass_yards;
                """
        cur.execute(qry)
        output = cur.fetchall()
        homeTeamResponse = output[0][0]
        awayTeamResponse = output[1][0]
        print("GetTotalPassingYards query result => ", (homeTeamResponse, awayTeamResponse))
        return (homeTeamResponse, awayTeamResponse)
        
    def GetAvgYardsPerPlay(self, request): 
        cur = self.conn.cursor()
        gameId = str(request.gameId)
        qry = f"""
                    WITH total_non_miss_yards_home AS (
                        SELECT COUNT(g.id) AS play_count, SUM(r.yard) as total_yards
                        FROM gridironrushes r
                        INNER JOIN gridirongameevents e ON r.eventId = e.id
                        INNER JOIN gridirongames g ON e.gameId = g.id
                        WHERE e.teamFor = g.home AND e.gameId = '{gameId}'
                        GROUP BY g.home

                        UNION ALL

                        SELECT COUNT(g.id) AS play_count, SUM(t.yard) as total_yards
                        FROM gridironthrows t
                        INNER JOIN gridirongameevents e ON t.eventId = e.id
                        INNER JOIN gridirongames g ON e.gameId = g.id
                        WHERE e.teamFor = g.home AND t.result != 'miss' AND e.gameId = '{gameId}'
                        GROUP BY g.home
                    ), 
                    total_non_miss_yards_away AS (
                        SELECT COUNT(g.id) AS play_count, SUM(r.yard) as total_yards
                        FROM gridironrushes r
                        INNER JOIN gridirongameevents e ON r.eventId = e.id
                        INNER JOIN gridirongames g ON e.gameId = g.id
                        WHERE e.teamFor = g.away AND e.gameId = '{gameId}'
                        GROUP BY g.away

                        UNION ALL

                        SELECT COUNT(g.id) AS play_count, SUM(t.yard) as total_yards
                        FROM gridironthrows t
                        INNER JOIN gridirongameevents e ON t.eventId = e.id
                        INNER JOIN gridirongames g ON e.gameId = g.id
                        WHERE e.teamFor = g.away AND t.result != 'miss' AND e.gameId = '{gameId}'
                        GROUP BY g.away
                    )
                    SELECT COALESCE((SELECT ROUND(SUM(total_yards)::numeric / SUM(play_count), 2)), 0)::numeric as avg_yards_per_play
                    FROM total_non_miss_yards_home
                    UNION ALL
                    SELECT COALESCE((SELECT ROUND(SUM(total_yards)::numeric / SUM(play_count), 2)), 0)::numeric as avg_yards_per_play
                    FROM total_non_miss_yards_away;
                """
        cur.execute(qry)
        output = cur.fetchall()
        homeTeamResponse = output[0][0]
        awayTeamResponse = output[1][0]
        print("GetAvgYardsPerPlay query result => ", (homeTeamResponse, awayTeamResponse))
        return (homeTeamResponse, awayTeamResponse)
        
    def GetTotalTouchdowns(self, request): 
        cur = self.conn.cursor()
        gameId = str(request.gameId)
        qry = f"""
                    WITH all_touchdowns_events AS (
                        SELECT eventId
                        FROM gridironrushes
                        WHERE result = 'touchdown'
                        UNION ALL
                        SELECT eventId
                        FROM gridironthrows
                        WHERE result = 'touchdown'
                    ),
                    touchdowns_home AS (
                        SELECT COUNT(g.id) AS touchdowns
                        FROM all_touchdowns_events td
                        INNER JOIN gridirongameevents e ON td.eventId = e.id
                        INNER JOIN gridirongames g ON e.gameId = g.id
                        WHERE e.teamFor = g.home AND e.gameId = '{gameId}'
                        GROUP BY g.home
                    ),
                    touchdowns_away AS (
                        SELECT COUNT(g.id) AS touchdowns
                        FROM all_touchdowns_events td
                        INNER JOIN gridirongameevents e ON td.eventId = e.id
                        INNER JOIN gridirongames g ON e.gameId = g.id
                        WHERE e.teamFor = g.away AND e.gameId = '{gameId}'
                        GROUP BY g.away
                    )
                    SELECT COALESCE((SELECT touchdowns), 0)::numeric as touchdowns
                    FROM touchdowns_home
                    UNION ALL
                    SELECT COALESCE((SELECT touchdowns), 0)::numeric as touchdowns
                    FROM touchdowns_away;
                """
        cur.execute(qry)
        output = cur.fetchall()
        homeTeamResponse = output[0][0]
        awayTeamResponse = output[1][0]
        print("GetTotalTouchdowns query result => ", (homeTeamResponse, awayTeamResponse))
        return (homeTeamResponse, awayTeamResponse)
        
    def GetTotalTurnovers(self, request): 
        cur = self.conn.cursor()
        gameId = str(request.gameId)
        qry = f"""
                    WITH home_turnovers AS (
                        SELECT COUNT(e.id) AS turnovers
                        FROM gridirongameevents e
                        INNER JOIN gridirongames g ON e.gameId = g.id
                        WHERE playType = 'turnover' AND e.teamFor = g.home AND e.gameId = '{gameId}'
                        GROUP BY g.home
                    ), away_turnovers AS (
                        SELECT COUNT(e.id) AS turnovers
                        FROM gridirongameevents e
                        INNER JOIN gridirongames g ON e.gameId = g.id
                        WHERE playType = 'turnover' AND e.teamFor = g.away AND e.gameId = '{gameId}'
                        GROUP BY g.away
                    )
                    SELECT COALESCE((SELECT * FROM home_turnovers), 0) AS turnovers
                    UNION ALL
                    SELECT COALESCE((SELECT * FROM away_turnovers), 0) AS turnovers;
                """
        cur.execute(qry)
        output = cur.fetchall()
        homeTeamResponse = output[0][0]
        awayTeamResponse = output[1][0]
        print("GetTotalTurnovers query result => ", (homeTeamResponse, awayTeamResponse))
        return (homeTeamResponse, awayTeamResponse)

    # League stats
    def GetTopFivePlayersByRushingYards(self, request):
        cur = self.conn.cursor()
        leagueId = str(request.leagueId)
        qry = f"""
                    SELECT r.player, SUM(r.yard) AS total_rushing_yards 
                    FROM gridironrushes r
                    INNER JOIN gridirongameevents e ON r.eventId = e.id
                    INNER JOIN gridirongames g ON e.gameId = g.id
                    INNER JOIN leagues l ON g.leagueId = l.id
                    WHERE l.id = '{leagueId}'
                    GROUP BY r.player
                    ORDER BY total_rushing_yards DESC
                    LIMIT 5;
                """
        cur.execute(qry)
        output = cur.fetchall()
        
        resp = []
        for i in range(len(output)): 
            resp.append(gridiron_pb2.GridironLeagueStatResponse(playerName=output[i][0], stat=float(output[i][1])))

        return resp

    def GetTopFivePlayersByReceivingYards(self, request):
        cur = self.conn.cursor()
        leagueId = str(request.leagueId)
        qry = f"""
                    SELECT t.playerReceiving, SUM(t.yard) AS total_receiving_yards 
                    FROM gridironthrows t
                    INNER JOIN gridirongameevents e ON t.eventId = e.id
                    INNER JOIN gridirongames g ON e.gameId = g.id
                    INNER JOIN leagues l ON g.leagueId = l.id
                    WHERE t.result!= 'miss' AND l.id = '{leagueId}'
                    GROUP BY t.playerReceiving
                    ORDER BY total_receiving_yards DESC
                    LIMIT 5;
                """
        cur.execute(qry)
        output = cur.fetchall()
        
        resp = []
        for i in range(len(output)): 
            resp.append(gridiron_pb2.GridironLeagueStatResponse(playerName=output[i][0], stat=float(output[i][1])))

        return resp

    def GetTopFivePlayersByThrowingYards(self, request):
        cur = self.conn.cursor()
        leagueId = str(request.leagueId)
        qry = f"""
                    SELECT t.playerThrowing, SUM(t.yard) AS total_throwing_yards 
                    FROM gridironthrows t
                    INNER JOIN gridirongameevents e ON t.eventId = e.id
                    INNER JOIN gridirongames g ON e.gameId = g.id
                    INNER JOIN leagues l ON g.leagueId = l.id
                    WHERE t.result!= 'miss' AND l.id = '{leagueId}'
                    GROUP BY t.playerThrowing
                    ORDER BY total_throwing_yards DESC
                    LIMIT 5;
                """
        cur.execute(qry)
        output = cur.fetchall()
        
        resp = []
        for i in range(len(output)): 
            resp.append(gridiron_pb2.GridironLeagueStatResponse(playerName=output[i][0], stat=float(output[i][1])))

        return resp

    def GetTopFivePlayersByKicksMade(self, request):
        cur = self.conn.cursor()
        leagueId = str(request.leagueId)
        qry = f"""
                    SELECT t.playerThrowing, ROUND(COUNT(CASE WHEN t.result != 'miss' THEN 1 ELSE NULL END)::numeric / COUNT(t.playerThrowing), 2) AS throw_completion_pct 
                    FROM gridironthrows t
                    INNER JOIN gridirongameevents e ON t.eventId = e.id
                    INNER JOIN gridirongames g ON e.gameId = g.id
                    INNER JOIN leagues l ON g.leagueId = l.id
                    WHERE l.id = '{leagueId}'
                    GROUP BY t.playerThrowing
                    ORDER BY throw_completion_pct DESC
                    LIMIT 5;
                """
        cur.execute(qry)
        output = cur.fetchall()
        
        resp = []
        for i in range(len(output)): 
            resp.append(gridiron_pb2.GridironLeagueStatResponse(playerName=output[i][0], stat=float(output[i][1])))

        return resp

    def GetTopFivePlayersByCompletionPercentage(self, request):
        cur = self.conn.cursor()
        leagueId = str(request.leagueId)
        qry = f"""
                    SELECT k.player, COUNT(k.player) AS total_kicks 
                    FROM gridironkicks k
                    INNER JOIN gridirongameevents e ON k.eventId = e.id
                    INNER JOIN gridirongames g ON e.gameId = g.id
                    INNER JOIN leagues l ON g.leagueId = l.id
                    WHERE k.result != 'miss' AND l.id = '{leagueId}'
                    GROUP BY k.player
                    ORDER BY total_kicks DESC
                    LIMIT 5;
                """
        cur.execute(qry)
        output = cur.fetchall()
        
        resp = []
        for i in range(len(output)): 
            resp.append(gridiron_pb2.GridironLeagueStatResponse(playerName=output[i][0], stat=float(output[i][1])))

        return resp
