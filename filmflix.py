##### |*************|SQLlie Python API|***************#####

# This program allows the user to add, update or delete records in the filmflix.db database.add()

import sqlite3


def userMenu():

    menu_choice = 0
    while menu_choice not in ["1", "2", "3", "4", "5"]:
        print("\nOptions menu")
        print("1. Add a record")
        print("2. Delete a record")
        print("3. Amend a record")
        print("4. Print all records")
        print("5. Exit")
        menu_choice = input("\nEnter your choice: ")
        if menu_choice not in ["1", "2", "3", "4", "5"]:
            print("Invalid choice")
    return menu_choice

# add records


def add():
    filmID = input("Input film ID: ")
    title = input("Input film title: ")
    yearReleased = input("Input year released: ")
    rating = input("Input rating (G, PG or R): ")
    try:
        duration = int(input("Input duration in minutes: "))
    except Exception:
        print("Duration must be an integer")
        return
    genre = input(
        "Input genre (Action, Animation, Fantasy, Comedy or Crime): ")
    film = [filmID, title, yearReleased, rating, duration, genre]
    with sqlite3.connect("filmflix.db") as conn:
        cursor = conn.cursor()
        try:
            cursor.execute('INSERT INTO tblFilms VALUES (?,?,?,?,?,?)', film)
            print("Film rec added:")
            for row in cursor.execute("Select * from tblFilms"):
                print(row)
        except Exception:
            print("""\n
A record with this ID already exists
Record has not been added
Make sure you enter a record with a unique ID
                  """)

 # amend record


def amend():
    with sqlite3.connect("filmflix.db") as conn:
        # or alternatively
        #   conn = sqlite3.connect("filmflix.db")
        #   with conn:
        cursor = conn.cursor()
        keyfield = input("Enter the ID of the record you want to amend: ")
        field = input(
            "Which field do you want to change (title, yearReleased,rating,duration,genre)? ")
        newvalue = input("Enter the new value for this field: ")
        newvalue = f"'{newvalue}'"
 #      enter a value as a string
 # You should validate it to make sure its an integer
        try:
            cursor.execute(
                f"UPDATE tblFilms SET {field}={newvalue} WHERE filmID ={keyfield}"
            )
 # note that if you use the statement "with sqlite3.connect("filmflix.db") as conn:" or equivalent
 # this automatically commits the changes so the commit() statement is not needed
 #           conn.commit()
            print("\nRecord updated")

        except Exception:
            print("\nNo record updated - invalid data entered")

 #  delete record


def delete():
    with sqlite3.connect("filmflix.db") as conn:
        cursor = conn.cursor()
        keyfield = input("Enter the ID of the record you want to delete: ")
        try:
            cursor.execute(f"DELETE FROM tblFilms WHERE filmID ={keyfield}")

            print("\nRecord deleted")
        except Exception:
            print("\nNo record with this ID  exists")

# print records


def printAll():
    with sqlite3.connect("filmflix.db") as conn:
        cursor = conn.cursor()
        for row in cursor.execute('SELECT * FROM tblFilms'):
            print(row)


# main
menu = True

while menu:
    choice = userMenu()
    if choice == "1":
        add()
    elif choice == "2":
        delete()
    elif choice == "3":
        amend()
    elif choice == "4":
        printAll()
    else:
        menu = False

input("Press Enter to exit program")
