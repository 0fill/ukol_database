import sqlite3

conn = sqlite3.connect("data.sql")
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS directors(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
birth_year INTEGER
)""")


c.execute("""CREATE TABLE IF NOT EXISTS movies(
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT NOT NULL,
release_year INTEGER,
genre TEXT,
director_id INTEGER,
FOREIGN KEY (director_id) REFERENCES directors(id));""")

c.execute("""CREATE TABLE IF NOT EXISTS actors(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
birth_year INTEGER
)""")


c.execute("""CREATE TABLE IF NOT EXISTS movie_actos(
movie_id INTEGER, 
actor_id INTEGER,
FOREIGN KEY(movie_id) REFERENCES movies(id),
FOREIGN KEY(actor_id) REFERENCES actors(id))
;""")

conn.commit()