#!/usr/bin/env python
from models.db_connection import DBConnection

# Initialize DB connection
db = DBConnection()

# === Input parameters ===
username = "test_user"
first_name = "Test"
last_name = "User"
phone_number = "0501234567"
home_address = "Tel Aviv"
id_number = "ID789"

# === Insert a user ===
db.execute("""
    INSERT INTO Users (
        UserName, FirstName, LastName, PhoneNumber, HomeAddress, ID
    ) VALUES (?, ?, ?, ?, ?, ?)
""", (username, first_name, last_name, phone_number, home_address, id_number), commit=True)

# === Fetch and print all users ===
users = db.execute("SELECT * FROM Users", fetchall=True)
for user in users:
    print(dict(user))