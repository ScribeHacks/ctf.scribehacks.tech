DROP TABLE IF EXISTS Challenges;

CREATE TABLE Challenges (
	ID integer PRIMARY KEY AUTOINCREMENT,
	Name varchar,
	Description text,
	Attachments text,
	Points integer,
	Answer varchar
);

DROP TABLE IF EXISTS Teams;

CREATE TABLE Teams (
	ID integer PRIMARY KEY AUTOINCREMENT, 
	TeamName varchar, 
	Score integer, 
	UserCount integer
);

DROP TABLE IF EXISTS Users;

CREATE TABLE Users (
	ID integer PRIMARY KEY AUTOINCREMENT,
	Username varchar,
	Team varchar
);