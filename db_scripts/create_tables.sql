CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
------------------------------------------------------------------

-- Create table users
CREATE TABLE users (
    id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    username character varying(80) NOT NULL UNIQUE,
    email character varying(255) NOT NULL UNIQUE,
    userpassword character varying(255) NOT NULL
);


CREATE INDEX IF NOT EXISTS users_pkey ON users(id uuid_ops);
CREATE INDEX IF NOT EXISTS users_username_key ON users(username text_ops);
CREATE INDEX IF NOT EXISTS users_email_key ON users(email text_ops);

------------------------------------------------------------------

-- Create table leagues
CREATE TABLE leagues (
    id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    league_name character varying(255) NOT NULL UNIQUE,
    league_password character varying(255) NOT NULL
);


CREATE INDEX IF NOT EXISTS leagues_pkey ON leagues(id uuid_ops);
CREATE INDEX IF NOT EXISTS leagues_league_name_key ON leagues(league_name text_ops);

------------------------------------------------------------------

-- Create table soccer game
CREATE TABLE soccergames (
    id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    home character varying(255) NOT NULL,
    away character varying(255) NOT NULL,
    starttime timestamp NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS soccer_pkey ON soccergames(id uuid_ops);

------------------------------------------------------------------

CREATE TABLE soccerevents (
    id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    EventType character varying(255) NOT NULL,
    GameId character varying(255) NOT NULL,
    SocEvent character varying(10000) NOT NULL,
    created_at timestamp DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS soccer_events_pkey ON soccerevents(id uuid_ops);

------------------------------------------------------------------

CREATE TABLE soccershots (
    id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    GameId uuid,
    IsGoal boolean,
	IsOnTarget boolean,
	Player character varying(255) NOT NULL,
	Assist character varying(255),
	soccershottime integer NOT NULL, 
	TeamFor character varying(255) NOT NULL,
	TeamAgainst character varying(255) NOT NULL
);

CREATE INDEX IF NOT EXISTS soccer_shots_pkey ON soccershots(id uuid_ops);

------------------------------------------------------------------

CREATE TABLE soccerfouls (
	id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
	GameId uuid,
	TeamFor character varying(255) NOT NULL,
	TeamAgainst character varying(255) NOT NULL,
	Player character varying(255) NOT NULL, 
	Reason character varying(255),
	IsYellow boolean,
	IsRed boolean,
	soccerfoultime integer
); 

CREATE INDEX IF NOT EXISTS soccer_fouls_pkey ON soccerfouls(id uuid_ops);

------------------------------------------------------------------

CREATE TABLE socceroffsides (
	id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
	GameId uuid,
	TeamFor character varying(255) NOT NULL,
	TeamAgainst character varying(255) NOT NULL,
    offsidetime integer NOT NULL
);

CREATE INDEX IF NOT EXISTS soccer_off_sides_pkey ON socceroffsides(id uuid_ops);

------------------------------------------------------------------
-- BASKETBALL
------------------------------------------------------------------

CREATE TABLE basketballgames (
    id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    leagueId uuid NOT NULL,
    home CHARACTER VARYING(255) NOT NULL,
    away CHARACTER VARYING(255) NOT NULL,
    starttime TIMESTAMP NOT NULL DEFAULT NOW(),

    CONSTRAINT fk_basketball_league FOREIGN KEY(leagueId) REFERENCES leagues(id)
);

-- postgres automatically indexes primary key + unique columns.
-- indexing PK just to be consistent with the previous DDL statements
CREATE INDEX IF NOT EXISTS basketball_pkey ON basketballgames(id uuid_ops);


------------------------------------------------------------------

CREATE TABLE basketballgameevents (
    id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    gameId uuid NOT NULL,
    playType CHARACTER VARYING(255) NOT NULL CHECK (playType IN (
        'point',
        'foul',
        'turnover',
        'timeout',
        'end',
        'block',
        'steal',
        'rebound'
    )),
    period SMALLINT NOT NULL CHECK (period IN (1,2,3,4)),
    teamFor CHARACTER VARYING(255),
    teamAgainst CHARACTER VARYING(255),

    CONSTRAINT fk_basketball_events_game FOREIGN KEY(gameId) REFERENCES basketballgames(id)
);

CREATE INDEX IF NOT EXISTS basketball_events_pkey ON basketballgameevents(id uuid_ops);
CREATE INDEX IF NOT EXISTS basketball_events_playtype ON basketballgameevents(playType text_ops);
CREATE INDEX IF NOT EXISTS basketball_events_period ON basketballgameevents(period int2_ops);

------------------------------------------------------------------

CREATE TABLE basketballpoints (
    id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    eventId uuid NOT NULL,
    player CHARACTER VARYING(255) NOT NULL,
    assist CHARACTER VARYING(255),
    result CHARACTER VARYING(255) NOT NULL CHECK (result IN (
        'made',
        'miss'
    )),
    point SMALLINT NOT NULL CHECK (point IN (1,2,3)),

    CONSTRAINT fk_basketball_points_event FOREIGN KEY(eventId) REFERENCES basketballgameevents(id)
);

CREATE INDEX IF NOT EXISTS basketball_events_pts_pkey ON basketballpoints(id uuid_ops);

------------------------------------------------------------------

CREATE TABLE basketballsteals (
    id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    eventId uuid NOT NULL,
    player CHARACTER VARYING(255) NOT NULL,

    CONSTRAINT fk_basketball_steals_event FOREIGN KEY(eventId) REFERENCES basketballgameevents(id)
);

CREATE INDEX IF NOT EXISTS basketball_events_steals_pkey ON basketballsteals(id uuid_ops);

------------------------------------------------------------------

CREATE TABLE basketballblocks (
    id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    eventId uuid NOT NULL,
    player CHARACTER VARYING(255) NOT NULL,

    CONSTRAINT fk_basketball_blocks_event FOREIGN KEY(eventId) REFERENCES basketballgameevents(id)
);

CREATE INDEX IF NOT EXISTS basketball_events_blocks_pkey ON basketballblocks(id uuid_ops);

------------------------------------------------------------------

CREATE TABLE basketballfouls (
    id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    eventId uuid NOT NULL,
    player CHARACTER VARYING(255) NOT NULL,
    reason CHARACTER VARYING(255),

    CONSTRAINT fk_basketball_fouls_event FOREIGN KEY(eventId) REFERENCES basketballgameevents(id)
);

CREATE INDEX IF NOT EXISTS basketball_events_fouls_pkey ON basketballfouls(id uuid_ops);

------------------------------------------------------------------

CREATE TABLE basketballturnovers (
    id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    eventId uuid NOT NULL,
    player CHARACTER VARYING(255) NOT NULL,

    CONSTRAINT fk_basketball_turnovers_event FOREIGN KEY(eventId) REFERENCES basketballgameevents(id)
);

CREATE INDEX IF NOT EXISTS basketball_events_turnovers_pkey ON basketballturnovers(id uuid_ops);

------------------------------------------------------------------

CREATE TABLE basketballrebounds (
    id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    eventId uuid NOT NULL,
    player CHARACTER VARYING(255) NOT NULL,

    CONSTRAINT fk_basketball_rebounds_event FOREIGN KEY(eventId) REFERENCES basketballgameevents(id)
);

CREATE INDEX IF NOT EXISTS basketball_events_rebounds_pkey ON basketballrebounds(id uuid_ops);

------------------------------------------------------------------

CREATE TABLE basketballgameends (
    id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    eventId uuid NOT NULL,
    ptsHome SMALLINT NOT NULL,
    ptsAway SMALLINT NOT NULL,

    CONSTRAINT fk_basketball_game_end_event FOREIGN KEY(eventId) REFERENCES basketballgameevents(id)
);

CREATE INDEX IF NOT EXISTS basketball_game_ends_pkey ON basketballgameends(id uuid_ops);

------------------------------------------------------------------
-- GRIDIRON FOOTBALL
------------------------------------------------------------------

CREATE TABLE gridirongames (
    id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    leagueId uuid NOT NULL,
    home CHARACTER VARYING(255) NOT NULL,
    away CHARACTER VARYING(255) NOT NULL,
    starttime TIMESTAMP NOT NULL DEFAULT NOW(),

    CONSTRAINT fk_gridiron_league FOREIGN KEY(leagueId) REFERENCES leagues(id)
);
-- postgres automatically indexes primary key + unique columns.
-- indexing PK just to be consistent with the previous DDL statements
CREATE INDEX IF NOT EXISTS gridiron_games_pkey ON gridirongames(id uuid_ops);

------------------------------------------------------------------

CREATE TABLE gridirongameevents (
    id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    gameId uuid NOT NULL,
    playType CHARACTER VARYING(255) NOT NULL CHECK (playType IN (
        'throw',
        'rush',
        'flag',
        'kick',
        'safety',
        'turnover',
        'timeout',
        'end'
    )),
    period SMALLINT NOT NULL CHECK (period IN (1,2,3,4)),
    teamFor CHARACTER VARYING(255),
    teamAgainst CHARACTER VARYING(255),

    CONSTRAINT fk_gridiron_events_game FOREIGN KEY(gameId) REFERENCES gridirongames(id)
);

CREATE INDEX IF NOT EXISTS gridiron_events_pkey ON gridirongameevents(id uuid_ops);
CREATE INDEX IF NOT EXISTS gridiron_events_playtype ON gridirongameevents(playType text_ops);
CREATE INDEX IF NOT EXISTS gridiron_events_period ON gridirongameevents(period int2_ops);

------------------------------------------------------------------

CREATE TABLE gridironrushes (
    id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    eventId uuid NOT NULL,
    player CHARACTER VARYING(255) NOT NULL,
    yard SMALLINT NOT NULL,
    result CHARACTER VARYING(255) NOT NULL CHECK (result IN (
        'touchdown',
        'non-scoring',
        '2pt'
    )),

    CONSTRAINT fk_gridiron_rush_event FOREIGN KEY(eventId) REFERENCES gridirongameevents(id)
);

CREATE INDEX IF NOT EXISTS gridiron_rushes_result ON gridironrushes(result text_ops);

------------------------------------------------------------------

CREATE TABLE gridironkicks (
    id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    eventId uuid NOT NULL,
    player CHARACTER VARYING(255) NOT NULL,
    yard SMALLINT NOT NULL,
    result CHARACTER VARYING(255) NOT NULL CHECK (result IN (
        'extra-kick',
        'field-goal',
        'miss'
    )),

    CONSTRAINT fk_gridiron_kick_event FOREIGN KEY(eventId) REFERENCES gridirongameevents(id)
);

CREATE INDEX IF NOT EXISTS gridiron_kicks_result ON gridironkicks(result text_ops);

------------------------------------------------------------------

CREATE TABLE gridironthrows (
    id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    eventId uuid NOT NULL,
    playerThrowing CHARACTER VARYING(255) NOT NULL,
    playerReceiving CHARACTER VARYING(255) NOT NULL,
    yard SMALLINT NOT NULL CHECK,
    result CHARACTER VARYING(255) NOT NULL CHECK (result IN (
        'touchdown',
        'non-scoring',
        '2pt',
        'miss'
    )),

    CONSTRAINT fk_gridiron_throw_event FOREIGN KEY(eventId) REFERENCES gridirongameevents(id)
);

CREATE INDEX IF NOT EXISTS gridiron_throws_result ON gridironthrows(result text_ops);

------------------------------------------------------------------

CREATE TABLE gridirongameends (
    id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    eventId uuid NOT NULL,
    ptsHome SMALLINT NOT NULL,
    ptsAway SMALLINT NOT NULL,

    CONSTRAINT fk_gridiron_game_ends_event FOREIGN KEY(eventId) REFERENCES gridirongameevents(id)
);

CREATE INDEX IF NOT EXISTS gridrion_game_ends_pkey ON gridirongameends(id uuid_ops);
