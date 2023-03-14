-- league-wide stats
-- top 5 points per game
SELECT p.player, ROUND(SUM(p.point)::numeric / COUNT(DISTINCT g.id), 2) AS points_per_game 
FROM basketballpoints p
INNER JOIN basketballgameevents e ON p.eventId = e.id
INNER JOIN basketballgames g ON e.gameId = g.id
INNER JOIN leagues l ON g.leagueId = l.id
WHERE p.result = 'made' AND l.id = '{leagueId}'
GROUP BY p.player
ORDER BY points_per_game DESC
LIMIT 5;

-- top 5 rebounds per game
SELECT r.player, ROUND(COUNT(r.player)::numeric / COUNT(DISTINCT g.id), 2) AS rebounds_per_game 
FROM basketballrebounds r
INNER JOIN basketballgameevents e ON r.eventId = e.id
INNER JOIN basketballgames g ON e.gameId = g.id
INNER JOIN leagues l ON g.leagueId = l.id
WHERE l.id = '{leagueId}'
GROUP BY r.player
ORDER BY rebounds_per_game DESC
LIMIT 5;

-- top 5 blocks per game
SELECT b.player, ROUND(COUNT(b.player)::numeric / COUNT(DISTINCT g.id), 2) AS blocks_per_game 
FROM basketballblocks b
INNER JOIN basketballgameevents e ON b.eventId = e.id
INNER JOIN basketballgames g ON e.gameId = g.id
INNER JOIN leagues l ON g.leagueId = l.id
WHERE l.id = '{leagueId}'
GROUP BY b.player
ORDER BY blocks_per_game DESC
LIMIT 5;

-- top 5 steals per game
SELECT s.player, ROUND(COUNT(s.player)::numeric / COUNT(DISTINCT g.id), 2) AS steals_per_game 
FROM basketballsteals s
INNER JOIN basketballgameevents e ON s.eventId = e.id
INNER JOIN basketballgames g ON e.gameId = g.id
INNER JOIN leagues l ON g.leagueId = l.id
WHERE l.id = '{leagueId}'
GROUP BY s.player
ORDER BY steals_per_game DESC
LIMIT 5;

-- top 5 assists per game
SELECT p.player, ROUND(COUNT(p.id)::numeric / COUNT(DISTINCT g.id), 2) AS assists_per_game 
FROM basketballpoints p
INNER JOIN basketballgameevents e ON p.eventId = e.id
INNER JOIN basketballgames g ON e.gameId = g.id
INNER JOIN leagues l ON g.leagueId = l.id
WHERE p.result = 'made' AND p.assist IS NOT NULL AND l.id = '{leagueId}'
GROUP BY p.player
ORDER BY assists_per_game DESC
LIMIT 5;

-- field goal pct
SELECT p.player, ROUND(COUNT(CASE WHEN p.result = 'made' then 1 else NULL end)::numeric / COUNT(p.id), 2) AS field_goal_percentage
FROM basketballpoints p
INNER JOIN basketballgameevents e ON e.id = p.eventId
INNER JOIN basketballgames g ON g.id = e.gameId
INNER JOIN leagues l ON g.leagueId = l.id
WHERE l.id = '{leagueId}'
GROUP BY p.player
ORDER by field_goal_percentage DESC
LIMIT 5;

-- 3pt percentage
SELECT p.player, ROUND(COUNT(CASE WHEN p.result = 'made' then 1 else NULL end)::numeric / COUNT(p.id), 2) AS three_points_percentage
FROM basketballpoints p
INNER JOIN basketballgameevents e ON p.eventId = e.id
INNER JOIN basketballgames g ON e.gameId = g.id
INNER JOIN leagues l ON g.leagueId = l.id
WHERE p.point = 3 AND l.id = '{leagueId}'
GROUP BY p.player
ORDER by three_points_percentage DESC
LIMIT 5;

-- query above will not return name of any players who hasn't attempted any 3 pt shots
-- is that okay?


-- free throw percentage
SELECT p.player,ROUND(COUNT(CASE WHEN p.result = 'made' then 1 else 0 end)::numeric / COUNT(p.id), 2) as free_throw_percentage
FROM basketballpoints p
INNER JOIN basketballgameevents e ON p.eventId = e.id
INNER JOIN basketballgames g ON e.gameId = g.id
INNER JOIN leagues l ON g.leagueId = l.id
WHERE p.point = 1 AND l.id = '{leagueId}'
GROUP BY p.player
ORDER by free_throw_percentage DESC
LIMIT 5;

-- query above will not return name of any players who hasn't attempted any 1 pt shots
-- is that okay?


-----------------
-- PER-GAME STATS
-----------------

-- FIELD GOAL PERCENTAGE --
WITH home_fgp AS (
    SELECT g.home, ROUND(COUNT(CASE WHEN p.result = 'made' then 1 else NULL end)::numeric / COUNT(p.id), 2) AS fgp
    FROM basketballpoints p
    INNER JOIN basketballgameevents e ON e.id = p.eventId
    INNER JOIN basketballgames g ON e.gameId = g.id
    WHERE e.teamFor = g.home AND g.id = '{gameId}'
    GROUP BY g.home
), away_fgp AS (
    -- Away team's field goal % for game.
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

-- 3PT PERCENTAGE --
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

-- FREE THROW PERCENTAGE --
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


-- TOTAL TURNOVERS --
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

-- TOTAL STEALS --
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

