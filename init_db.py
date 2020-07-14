import sqlite3
import os
from dotenv import load_dotenv
load_dotenv()

connection = sqlite3.connect('database.db')
FLAG_1 = os.getenv("FLAG_1")

cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS Challenges")
cursor.execute('CREATE TABLE Challenges (ID integer PRIMARY KEY AUTOINCREMENT, Name varchar, Description text, Attachments text, Points integer, Answer text)')
cursor.execute(f"INSERT INTO Challenges VALUES (1, 'The Curse of the Grave', 'Figure out how to revive the fallen grandfather clock in an accident caused by the ghost of long past','',100, '{FLAG_1}')")
cursor.execute("DROP TABLE IF EXISTS Teams")
cursor.execute("CREATE TABLE Teams (ID integer PRIMARY KEY AUTOINCREMENT, TeamName varchar, Score integer)")
cursor.execute(f"INSERT INTO Teams VALUES (1, 'The Banana Splits', 200)")

challenges = cursor.execute("SELECT ID, Name, Description, Attachments, Points, Answer FROM Challenges").fetchall()
teams = cursor.execute("SELECT ID, TeamName, Score FROM Teams").fetchall()
print(challenges)
print(teams)


# connection.commit()
# connection.close()

