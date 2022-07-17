-- Create table users
CREATE TABLE users (
    id uuid PRIMARY KEY,
    username character varying(80) NOT NULL UNIQUE,
    email character varying(255) NOT NULL UNIQUE,
    password character varying(255) NOT NULL
);

-- Indices -------------------------------------------------------

CREATE UNIQUE INDEX users_pkey ON users(id uuid_ops);
CREATE UNIQUE INDEX users_username_key ON users(username text_ops);
CREATE UNIQUE INDEX users_email_key ON users(email text_ops);

-- Create table leagues
CREATE TABLE leagues (
    id uuid PRIMARY KEY,
    league_name character varying(255) NOT NULL UNIQUE,
    league_password character varying(255) NOT NULL
);

-- Indices -------------------------------------------------------

CREATE UNIQUE INDEX leagues_pkey ON leagues(id uuid_ops);
CREATE UNIQUE INDEX leagues_league_name_key ON leagues(league_name text_ops);

-- Create table soccer game
CREATE TABLE soccergames (
    id uuid PRIMARY KEY,
    home character varying(255) NOT NULL,
    away character varying(255) NOT NULL,
    starttime datetime NOT NULL
);

-- Indices

CREATE UNIQUE INDEX soccer_pkey ON soccergames(id uuid_ops);

CREATE TABLE soccerevents (
    id uuid PRIMARY KEY,
    EventType character varying(255) NOT NULL,
    GameId character varying(255) NOT NULL,
    SocEvent blob(255) NOT NULL,
);

CREATE UNIQUE INDEX soccer_events_pkey ON soccerevents(id uuid_ops);


CREATE TABLE soccershots (
    id uuid PRIMARY KEY,
    GameId uuid,
    IsGoal boolean,
	IsOnTarget boolean,
	Player character varying(255) NOT NULL,
	Assist character varying(255) NOT NULL,
	Time integer NOT NULL, 
	TeamFor character varying(255) NOT NULL,
	TeamAgainst character varying(255) NOT NULL,
);

CREATE UNIQUE INDEX soccer_shots_pkey ON soccershots(id uuid_ops);

CREATE TABLE soccerfouls (
	Id uuid PRIMARY KEY,
	GameId uuid,
	TeamFor character varying(255) NOT NULL,
	TeamAgainst character varying(255) NOT NULL,
	Player character varying(255) NOT NULL, 
	Reason character varying(255) NOT NULL,
	IsYellow boolean,
	IsRed boolean,
	Time integer NOT NULL,
); 

CREATE UNIQUE INDEX soccer_fouls_pkey ON soccerfouls(id uuid_ops);

CREATE TABLE socceroffsides (
	Id uuid PRIMARY KEY,
	GameId uuid,
	TeamFor character varying(255) NOT NULL,
	TeamAgainst character varying(255) NOT NULL,
	Time integer NOT NULL,
);

CREATE UNIQUE INDEX soccer_off_sides_pkey ON socceroffsides(id uuid_ops);






