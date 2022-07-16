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



