import sqlite3

conn = sqlite3.connect("players.db")
cursor = conn.cursor()


table_creation = """
    CREATE TABLE PLAYERS (
        Name CHAR(46) NOT NULL,
        Team CHAR(5) NOT NULL,
        Conference CHAR(4) NOT NULL,
        Division CHAR(15) NOT NULL,
        Position CHAR(5) NOT NULL,
        Height INT NOT NULL,
        Age INT NOT NULL,
        Number INT NOT NULL
    );
"""

cursor.execute(table_creation)
