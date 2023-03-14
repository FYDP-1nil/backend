------
-- PER LEAGUE STATS
------
-- TOP 5 PLAYERS BY TOTAL RUSHING YARDS -> (player: str, rushes: int) x5
SELECT r.player, SUM(r.yard) AS total_rushing_yards 
FROM gridironrushes r
INNER JOIN gridirongameevents e ON r.eventId = e.id
INNER JOIN gridirongames g ON e.gameId = g.id
INNER JOIN leagues l ON g.leagueId = l.id
WHERE l.id = 'ea4bc412-c6e3-40e9-9753-275730216d50'
GROUP BY r.player
ORDER BY total_rushing_yards DESC
LIMIT 5;

-- TOP 5 PLAYERS BY TOTAL RECEIVING YARDS -> (player: str, yards: int) x5
SELECT t.playerReceiving, SUM(t.yard) AS total_receiving_yards 
FROM gridironthrows t
INNER JOIN gridirongameevents e ON t.eventId = e.id
INNER JOIN gridirongames g ON e.gameId = g.id
INNER JOIN leagues l ON g.leagueId = l.id
WHERE t.result!= 'miss' AND l.id = 'ea4bc412-c6e3-40e9-9753-275730216d50'
GROUP BY t.playerReceiving
ORDER BY total_receiving_yards DESC
LIMIT 5;

-- TOP 5 PLAYERS BY TOTAL THROWING YARDS -> (player: str, yards: int) x5
SELECT t.playerThrowing, SUM(t.yard) AS total_throwing_yards 
FROM gridironthrows t
INNER JOIN gridirongameevents e ON t.eventId = e.id
INNER JOIN gridirongames g ON e.gameId = g.id
INNER JOIN leagues l ON g.leagueId = l.id
WHERE t.result!= 'miss' AND l.id = 'ea4bc412-c6e3-40e9-9753-275730216d50'
GROUP BY t.playerThrowing
ORDER BY total_throwing_yards DESC
LIMIT 5;

-- TOP 5 PLAYERS BY THROW COMPLETION PERCENTAGE -> (player: str, percentage: float) x5
SELECT t.playerThrowing, ROUND(COUNT(CASE WHEN t.result != 'miss' THEN 1 ELSE NULL END)::numeric / COUNT(t.playerThrowing), 2) AS throw_completion_pct 
FROM gridironthrows t
INNER JOIN gridirongameevents e ON t.eventId = e.id
INNER JOIN gridirongames g ON e.gameId = g.id
INNER JOIN leagues l ON g.leagueId = l.id
WHERE l.id = 'ea4bc412-c6e3-40e9-9753-275730216d50'
GROUP BY t.playerThrowing
ORDER BY throw_completion_pct DESC
LIMIT 5;

-- TOP 5 PLAYERS BY TOTAL KICKS -> (player: str, kicks: int) x5
SELECT k.player, COUNT(k.player) AS total_kicks 
FROM gridironkicks k
INNER JOIN gridirongameevents e ON k.eventId = e.id
INNER JOIN gridirongames g ON e.gameId = g.id
INNER JOIN leagues l ON g.leagueId = l.id
WHERE k.result != 'miss' AND l.id = 'ea4bc412-c6e3-40e9-9753-275730216d50'
GROUP BY k.player
ORDER BY total_kicks DESC
LIMIT 5;



------
-- PER GAME STATS
------

-- TOTAL RUSHING YARDS --
WITH home_rush_yards AS (
    SELECT SUM(r.yard) AS rush_yards
    FROM gridironrushes r
    INNER JOIN gridirongameevents e ON r.eventId = e.id
    INNER JOIN gridirongames g ON e.gameId = g.id
    WHERE e.teamFor = g.home AND e.gameId = 'dde41514-e573-42ba-86de-32d48a4bdda8'
    GROUP BY g.home
), away_rush_yards AS (
    SELECT SUM(r.yard) AS rush_yards
    FROM gridironrushes r
    INNER JOIN gridirongameevents e ON r.eventId = e.id
    INNER JOIN gridirongames g ON e.gameId = g.id
    WHERE e.teamFor = g.away AND e.gameId = 'dde41514-e573-42ba-86de-32d48a4bdda8'
    GROUP BY g.away
)
SELECT COALESCE((SELECT * FROM home_rush_yards), 0) AS rush_yards
UNION ALL
SELECT COALESCE((SELECT * FROM away_rush_yards), 0) AS rush_yards;


-- TOTAL PASSING YARDS --
WITH home_pass_yards AS (
    SELECT SUM(t.yard) AS pass_yards
    FROM gridironthrows t
    INNER JOIN gridirongameevents e ON t.eventId = e.id
    INNER JOIN gridirongames g ON e.gameId = g.id
    WHERE e.teamFor = g.home AND t.result != 'miss' AND e.gameId = 'dde41514-e573-42ba-86de-32d48a4bdda8'
    GROUP BY g.home
), away_pass_yards AS (
    SELECT SUM(t.yard) AS pass_yards
    FROM gridironthrows t
    INNER JOIN gridirongameevents e ON t.eventId = e.id
    INNER JOIN gridirongames g ON e.gameId = g.id
    WHERE e.teamFor = g.away AND t.result != 'miss' AND e.gameId = 'dde41514-e573-42ba-86de-32d48a4bdda8'
    GROUP BY g.away
)
SELECT COALESCE((SELECT * FROM home_pass_yards), 0) AS pass_yards
UNION ALL
SELECT COALESCE((SELECT * FROM away_pass_yards), 0) AS pass_yards;


-- AVG YARDS PER PLAY --
WITH total_non_miss_yards_home AS (
    SELECT COUNT(g.id) AS play_count, SUM(r.yard) as total_yards
    FROM gridironrushes r
    INNER JOIN gridirongameevents e ON r.eventId = e.id
    INNER JOIN gridirongames g ON e.gameId = g.id
    WHERE e.teamFor = g.home AND e.gameId = 'dde41514-e573-42ba-86de-32d48a4bdda8'
    GROUP BY g.home

    UNION ALL

    SELECT COUNT(g.id) AS play_count, SUM(t.yard) as total_yards
    FROM gridironthrows t
    INNER JOIN gridirongameevents e ON t.eventId = e.id
    INNER JOIN gridirongames g ON e.gameId = g.id
    WHERE e.teamFor = g.home AND t.result != 'miss' AND e.gameId = 'dde41514-e573-42ba-86de-32d48a4bdda8'
    GROUP BY g.home
), 
total_non_miss_yards_away AS (
    SELECT COUNT(g.id) AS play_count, SUM(r.yard) as total_yards
    FROM gridironrushes r
    INNER JOIN gridirongameevents e ON r.eventId = e.id
    INNER JOIN gridirongames g ON e.gameId = g.id
    WHERE e.teamFor = g.away AND e.gameId = 'dde41514-e573-42ba-86de-32d48a4bdda8'
    GROUP BY g.away

    UNION ALL

    SELECT COUNT(g.id) AS play_count, SUM(t.yard) as total_yards
    FROM gridironthrows t
    INNER JOIN gridirongameevents e ON t.eventId = e.id
    INNER JOIN gridirongames g ON e.gameId = g.id
    WHERE e.teamFor = g.away AND t.result != 'miss' AND e.gameId = 'dde41514-e573-42ba-86de-32d48a4bdda8'
    GROUP BY g.away
)
SELECT COALESCE((SELECT ROUND(SUM(total_yards)::numeric / SUM(play_count), 2)), 0)::numeric as avg_yards_per_play
FROM total_non_miss_yards_home
UNION ALL
SELECT COALESCE((SELECT ROUND(SUM(total_yards)::numeric / SUM(play_count), 2)), 0)::numeric as avg_yards_per_play
FROM total_non_miss_yards_away;

-- TOTAL TOUCHDOWNS --
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
    WHERE e.teamFor = g.home AND e.gameId = 'dde41514-e573-42ba-86de-32d48a4bdda8'
    GROUP BY g.home
),
touchdowns_away AS (
    SELECT COUNT(g.id) AS touchdowns
    FROM all_touchdowns_events td
    INNER JOIN gridirongameevents e ON td.eventId = e.id
    INNER JOIN gridirongames g ON e.gameId = g.id
    WHERE e.teamFor = g.away AND e.gameId = 'dde41514-e573-42ba-86de-32d48a4bdda8'
    GROUP BY g.away
)
SELECT COALESCE((SELECT touchdowns), 0)::numeric as touchdowns
FROM touchdowns_home
UNION ALL
SELECT COALESCE((SELECT touchdowns), 0)::numeric as touchdowns
FROM touchdowns_away;

-- TOTAL TURNOVERS --
WITH home_turnovers AS (
    SELECT COUNT(e.id) AS turnovers
    FROM gridirongameevents e
    INNER JOIN gridirongames g ON e.gameId = g.id
    WHERE playType = 'turnover' AND e.teamFor = g.home AND e.gameId = 'dde41514-e573-42ba-86de-32d48a4bdda8'
    GROUP BY g.home
), away_turnovers AS (
    SELECT COUNT(e.id) AS turnovers
    FROM gridirongameevents e
    INNER JOIN gridirongames g ON e.gameId = g.id
    WHERE playType = 'turnover' AND e.teamFor = g.away AND e.gameId = 'dde41514-e573-42ba-86de-32d48a4bdda8'
    GROUP BY g.away
)
SELECT COALESCE((SELECT * FROM home_turnovers), 0) AS turnovers
UNION ALL
SELECT COALESCE((SELECT * FROM away_turnovers), 0) AS turnovers;
