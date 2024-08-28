def add_director(name, birth_year, cursor):
    cursor.execute(f"""INSERT INTO directors
              VALUES ({name}, {birth_year});""")


def add_actor(name, birth_year, cursor):
    cursor.execute(f"""INSERT INTO actors
                        VALUES ({name}, {birth_year});""")


def add_films(title, release_year, genre, director_id, cursor, actors: tuple):
    cursor.execute(f"""INSERT INTO movies (title, release_year, genre, director_id)
                    VALUES (?,?,?,?);""", (title, release_year, genre, director_id,))

    placeholders = ', '.join('?' * len(actors))
    CODE = f"""INSERT INTO movie_actors (movie_id, actor_id)
                        SELECT
                            movies.id AS movie_id,
                            actors.id AS actor_id
                        FROM
                            movies
                        INNER JOIN actors ON actors.name IN ({placeholders})
                        WHERE
                            movies.title = ?                            
                            ;"""
    a = actors+(title,)
    cursor.execute(CODE, a)



def search_film_name(name, cursor):
    cursor.execute(f"""SELECT * FROM movies
                        WHERE title LIKE ?;""",
                   (f"%{name}%",))
    return cursor.fetchall()


def search_film_year(year, cursor):
    cursor.execute(f"""SELECT * FROM movies
                                WHERE ? = release_year;""",
                   (year,))
    return cursor.fetchall()


def search_film_genre(genre, cursor):
    cursor.execute(f"""SELECT * FROM movies
                               WHERE genre LIKE %?%;""",
                   (genre,))
    return cursor.fetchall()


def search_film_director(director, cursor):
    cursor.execute(f"""SELECT 
            movies.*
        FROM 
            movies
        INNER JOIN 
            directors ON movies.director_id = directors.director_id
        WHERE 
            directors.name = %?%;
                        """,(director,))
    return cursor.fetchall()


def search_film_actor(actor: str, cursor):
    cursor.execute(f"""SELECT 
            movies.*
        FROM 
            movies
        INNER JOIN 
            movie_actors ON movies.id = movie_actors.movie_id
        INNER JOIN 
            actors ON actors.id = movie_actors.director_id
        WHERE 
            actors.name = ?;
    """, (actor,))
    return cursor.fetchall()


def list_films(cursor):
    cursor.execute("""
        SELECT 
            movies.*,
            directors.name AS director_name,
            actors.name AS actor_name
        FROM 
            movies
        INNER JOIN 
            directors ON directors.id = movies.director_id
        LEFT JOIN 
            movie_actors ON movies.id = movie_actors.movie_id
        LEFT JOIN 
            actors ON actors.id = movie_actors.actor_id
    """)
    return cursor.fetchall()


def test_director(director: str, cursor):
    cursor.execute(f"""
            SELECT id 
            FROM directors 
            WHERE name = ?
        """, (director,))
    return cursor.fetchall()


def test_actor(actor: str, cursor):
    cursor.execute(f"""SELECT name FROM actors
                        WHERE name = ?""",
                   (actor,))
    return cursor.fetchall()
