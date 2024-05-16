from bin.db import DBManager

import random
from psycopg2.errors import DuplicateTable


DB_NAME = "test_db"
TABLES = {
    "rents": [["id", "room_id", "transaction_id", "since", "due"], ["SERIAL PRIMARY KEY", "int", "int", "date", "date"]],
    "rooms": [["id", "price", "capacity"], ["SERIAL PRIMARY KEY", "real", "int"]],
    "transactions": [["id", "details", "sum", "completed"], ["SERIAL PRIMARY KEY", "text", "real", "bool"]],
    "clients": [["id", "password_hash", "username", "fio", "credentials"], ["SERIAL PRIMARY KEY", "varchar(16)", "varchar(64)", "varchar(128)", "varchar(12)"]],
    "clients_rents": [["client_id", "rent_id"], ["int", "int"]],
    "sales": [["id", "client_id", "percent"], ["SERIAL PRIMARY KEY", "int", "real"]],
}
USER = "test"

db = DBManager(db_name=DB_NAME, user=USER)
db.connect()

def init_tables():
    for name, columns_types in TABLES.items():
        columns, types = columns_types
        try:
            db.create_table(name, columns, types, temporary=False)
        except DuplicateTable:
            print("Table {} already exist".format(name))

    db.commit

def fill_tables_with_test_data():
    for _ in range(10):
        price, capacity = random.randint(1, 10) * 1_000, random.randint(1, 7)
        db.execute("INSERT INTO rooms (price, capacity) VALUES ({}, {})".format(price, capacity))
    db.execute("INSERT INTO rents (room_id, transaction_id, since, due) VALUES (1, 1, '2000-01-01', '2000-02-02')")
    db.execute("INSERT INTO transactions (details, sum, completed) VALUES ('some info', 100, True)")
    db.execute("INSERT INTO clients (password_hash, username, fio, credentials) VALUES ('*#@(RJOFSO)', 'example', 'A B C', '000000000000')")
    db.execute("INSERT INTO clients_rents (client_id, rent_id) VALUES (1, 1)")
    db.execute("INSERT INTO sales (client_id, percent) VALUES (1, 10)")
    db.commit()

def drop_tables():
    for name, _ in TABLES.items():
        db.execute("DROP TABLE {}".format(name))

    db.commit()

def show_tables():
    res = []

    for name in TABLES.keys():
        db.execute("SELECT * FROM {} LIMIT 10".format(name))
        res.append("{}: {}".format(name, db.fetch()))

    print(*res, sep="\n")

actions = [
    init_tables,
    fill_tables_with_test_data,
    show_tables,
    drop_tables,
]

choice = ""
while True:
    print("0. Init tables")
    print("1. Fill tables")
    print("2. Show tables")
    print("3. Drop tables")

    try:
        choice = int(input("Choice: "))
    except TypeError:
        continue

    try:
        actions[choice]()
    except IndexError:
        continue
