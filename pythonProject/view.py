from control import *


def main_menu():
    print("\tWelcome to Main Menu\n"
          "\t  /Main Menu\\\n"
          "\t1-add to databse\n"
          "\t2-search in databse\n"
          "\t3-exit database\n             ")


def get_choice(min: int = 1, max: int = 3):
    while True:
        choice = input("\n")
        try:
            choice = int(choice)
        except ValueError:
            print("Please enter an number")
            continue
        if choice not in range(min, max):
            print("Invalid choice")
            continue
        return choice


def menu_add():
    print("\t1. add film to database\n"
          "\t2. add director to database\n"
          "\t3. add actor to database\n")


def menu_display():
    print("""\t\t1. show everything
    \t\t2. search in database by name of film
    \t\t3. search in database by year of releas
    \t\t4. search in database by genre
    \t\t5. search in database by director
    \t\t6. search in database by actor
    """)


def check_director(cursor):
    while True:
        director = input("Enter directors name: ")
        res = test_director(director, cursor)
        if not res:
            continue
        return director


def check_actors(cursor):
    actors = []
    while True:
        temp = input("Enter actor name: ")
        if len(test_actor(temp, cursor)) > 0:
            actors.append(temp)
        else:
            print("Invalid actor")
        if input("Do you want to add another actor?(y/n)") == "y":
            continue
        else:
            return tuple(actors)


def get_film(cursor):  #adding film
    name = input("Enter Film Name: ")
    year = input("Enter Year of releas: ")
    genre = input("Enter Genre: ")
    director_id: int = check_director(cursor)
    actors: tuple = check_actors(cursor)  #tuple of names
    return name, year, genre, director_id, actors


def get_director():
    name = input("Enter his/her name: ")
    while True:
        year = input("Enter Year of birth: ")
        try:
            year = int(year)
            break
        except ValueError:
            print("Invalid year")
    return name, year


def get_actor():
    name = input("Enter his/her name: ")
    while True:
        year = input("Enter Year of birth: ")
        try:
            year = int(year)
            break
        except ValueError:
            print("Invalid year")
    return name, year


def get_film_name():
    while True:
        name = input("Enter Film Name: ")
        return name


def display_films(films: tuple):
    for film in films:
        for i in film:
            print(i, end="\t")
        print()


def get_year():
    while True:
        year = input("Enter year of releas: ")
        try:
            year = int(year)
            return year
        except ValueError:
            print("Invalid year")


def get_genre():
    return input("Enter genre: ")
