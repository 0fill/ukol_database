import sqlite3

conn = sqlite3.connect("data.sql")
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS movies(
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT NOT NULL,
release_year INTEAGER,
genre TEXT,
director_id INTEAGER FOREIGN KEY(director_id) REFERENCES directors(id),
)""")

c.execute("""CREATE TABLE IF NOT EXISTS actors(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
birth_year INTEGER
)""")

c.execute("""CREATE TABLE IF NOT EXISTS directors(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
birth_year INTEGER
)""")

c.execute("""CREATE TABLE IF NOT EXISTS movie_actos(
movie_id INTEAGER FOREIGN KEY(movie_id) REFERENCES movies(id),
actor_id INTEGER REFERENCES actors(id) REFERENCES actors(id),
""")