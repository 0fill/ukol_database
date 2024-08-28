import sqlite3
from models import *
from control import *
from view import *

database = database("data.sql")
cur = database.conn.cursor()


def run(cursor):
    while True:
        main_menu()
        choice = get_choice(0, 3)
        if choice == 1:  #pridat
            menu_add()
            choice = get_choice(1, 3)
            if choice == 1:  #pridam film
                a, b, c, d, e = get_film(cursor)
                add_films(a, b, c, d,cursor, e)
            elif choice == 2:  #pridam rezisera
                a, b = get_director()
                add_director(a, b)
            elif choice == 3:  #pridam herce
                a, b = get_actor()
                add_actor(a, b, cursor)
            else:
                continue
            database.conn.commit()
        elif choice == 2:  #zobrazit
            menu_display()
            choice = get_choice(1, 6)
            if choice == 1:  #zobrazit vse
                display_films(list_films(cursor))
            elif choice == 2:  #zobrazit podle jmena
                a = get_film_name()
                display_films(search_film_name(a, cursor))
            elif choice == 3:  #zobrazit podle roku
                a = get_year()
                display_films(search_film_year(a, cursor))
            elif choice == 4:  #zobrazit podle zanru
                a = get_genre()
                display_films(search_film_genre(a, cursor))
            elif choice == 5:  #zobrazit podle razisera
                a = get_director
                display_films(search_film_genre(a, cursor))
            elif choice == 6:  #zobrazit podle hercu
                a = get_actor()
                display_films(search_film_actor(a, cursor))
            else:
                continue
        elif choice == 3:  #exit
            break
        elif choice == 0:
            database.insert_test_data(cur)


run(cur)
