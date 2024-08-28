import sqlite3


class database:
    def __init__(self,database_name):
        self.conn = sqlite3.connect("data.sql")
        c = self.conn.cursor()

        c.execute("""CREATE TABLE IF NOT EXISTS directors(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        birth_year INTEGER
        )""")

        c.execute("""CREATE TABLE IF NOT EXISTS movies(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        release_year INTEGER,d
        genre TEXT,
        director_id INTEGER,
        FOREIGN KEY (director_id) REFERENCES directors(id));""")

        c.execute("""CREATE TABLE IF NOT EXISTS actors(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        birth_year INTEGER
        )""")

        c.execute("""CREATE TABLE IF NOT EXISTS movie_actors(
        movie_id INTEGER, 
        actor_id INTEGER,
        FOREIGN KEY(movie_id) REFERENCES movies(id),
        FOREIGN KEY(actor_id) REFERENCES actors(id))
        ;""")
        c.close()
        self.conn.commit()


    def insert_test_data(self,cursor):
        # Insert data into directors table
        cursor.execute("""
            INSERT INTO directors (name, birth_year) VALUES
            ('Steven Spielberg', 1946),
            ('Martin Scorsese', 1942),
            ('Quentin Tarantino', 1963)
        """)

        # Insert data into movies table
        cursor.execute("""
            INSERT INTO movies (title, release_year, genre, director_id) VALUES
            ('Jurassic Park', 1993, 'Adventure', 1),
            ('Goodfellas', 1990, 'Crime', 2),
            ('Pulp Fiction', 1994, 'Crime', 3)
        """)

        # Insert data into actors table
        cursor.execute("""
            INSERT INTO actors (name, birth_year) VALUES
            ('Sam Neill', 1947),
            ('Robert De Niro', 1943),
            ('John Travolta', 1954)
        """)

        # Insert data into movie_actors table
        cursor.execute("""
            INSERT INTO movie_actors (movie_id, actor_id) VALUES
            (1, 1),  -- Jurassic Park with Sam Neill
            (2, 2),  -- Goodfellas with Robert De Niro
            (3, 3)   -- Pulp Fiction with John Travolta;""")
        self.conn.commit()