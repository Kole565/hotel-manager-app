from db import DB


DB_NAME = "test_db"
# USER = input("Enter username: ")
USER = "test"


db = DB(db_name=DB_NAME, user=USER)
db.connect()

def show_table():
    name = input("Enter table name: ")

    db.execute("")
    db.execute("SELECT * FROM {} LIMIT 10".format(name))

options = [
    "Show table",
    "Remove client",
    "Register client",
    "Create rent",
    "Modify rent",
    "Create room",
    "Modify room",
]
actions = [
    lambda: print("Not implemented"),
    lambda: print("Not implemented"),
    lambda: print("Not implemented"),
    lambda: print("Not implemented"),
    lambda: print("Not implemented"),
    lambda: print("Not implemented"),
    lambda: print("Not implemented"),
]

choice = ""
while True:
    print(*["{}. {}".format(int(index) + 1, option) for index, option,  in enumerate(options)], sep="\n", end="\n\n")

    try:
        choice = int(input("Choice: ")) - 1
    except TypeError:
        continue

    try:
        actions[choice]()
    except IndexError:
        continue
