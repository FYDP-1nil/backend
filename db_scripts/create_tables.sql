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

CREATE INDEX IF NOT EXISTS basketball_events_turnovers_pkey ON basketballrebounds(id uuid_ops);

------------------------------------------------------------------

CREATE TABLE basketballgameends (
    id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    eventId uuid NOT NULL,
    ptsHome SMALLINT NOT NULL,
    ptsAway SMALLINT NOT NULL,

    CONSTRAINT fk_basketball_turnovers_event FOREIGN KEY(eventId) REFERENCES basketballgameevents(id)
);

CREATE INDEX IF NOT EXISTS basketball_events_turnovers_pkey ON basketballblocks(id uuid_ops);
