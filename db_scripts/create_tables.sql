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
    SocEvent bytea NOT NULL,
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
	Assist character varying(255) NOT NULL,
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
	Reason character varying(255) NOT NULL,
	IsYellow boolean,
	IsRed boolean,
	soccerfoultime integer NOT NULL
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






