DROP TABLE IF EXISTS Challenges;

CREATE TABLE Challenges (
	ID integer PRIMARY KEY AUTOINCREMENT,
	Name varchar,
	Description text,
	Attachments text,
	Points integer,
	Answer varchar
);

