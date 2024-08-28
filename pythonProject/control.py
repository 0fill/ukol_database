def insert_directors(name, birth_year,cursor=c):
    cursor.execute(f"""INSERT INTO directors
              VALUES ({name}, {birth_year});""")

def insert_actors(name, birth_year,cursor=c):
    cursor.execute(f"""INSERT INTO actors
                        VALUES ({name}, {birth_year});""")

def insert_films(title,release_year, genre, director_id,cursor,actors:tuple):
    cursor.execute(f"""INSERT INTO movies
                    VALUES ({title},{release_year},{genre},{director_id});""")
    cursor.execute(f"""INSERT INTO movie_actors (movie_id, actor_id)
                        SELECT 
                            movies.id AS movie_id,
                            actors.id AS actor_id
                        FROM 
                            movies
                            INNER JOIN actors ON a.name IN ({actors})
                        WHERE 
                            movie.title = '{title}';""")

def search_film_name(name,cursor=c):
    cursor.execute(f"""SELECT * FROM movie_actors
                        WHERE name LIKE '%{name}%';""")
    return cursor.fetchall()
def search_film_year(year,cursor=c):
    cursor.execute(f"""SELECT * FROM movies
                                WHERE {year} = release_year;""")
    return cursor.fetchall()
def search_film_genre(genre,cursor=c):
    cursor.execute(f"""SELECT * FROM movies
                               WHERE genre LIKE '%{genre}%';""")
    return cursor.fetchall()
def search_film_director(director,cursor=c):
    cursor.execute(f"""SELECT 
            movies.*
        FROM 
            movies
        INNER JOIN 
            directors ON movies.director_id = directors.director_id
        WHERE 
            directors.name = %{director}%;
                        """)
    return cursor.fetchall()

def search_film_actor(actor: str,cursor=c):
    cursor.execute(f"""SELECT 
            movies.*
        FROM 
            movies
        INNER JOIN 
            movie_actors ON movies.id = movie_actors.movie_id
        INNER JOIN 
            actors ON actors.id = movie_actors.director_id
        WHERE 
            actors.name = {actor};
    """)
    return cursor.fetchall()

def list_films(cursor=c):
    cursor.execute(f"""SELECT 
            movies.*
            drectors.name
            actors.name
        FROM 
            movies
        INNER JOIN 
            movie_actors ON movies.id = movie_actors.movie_id
        INNER JOIN 
            directors ON directors.id = movie_actors.director_id
        INNER JOIN 
            actors ON actors.id = movie_actors.actor_id
    ;""")
    return cursor.fetchall()