import requests
import sys
import os
# from models import db_connection as DBConnection
# Add the root directory of your project to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from models.db_connection import DBConnection
import json

def test_fetch_user():
    db = DBConnection()

    # Test user input
    test_data = {
        "username": "test_user_pytest",
        "first_name": "Py",
        "last_name": "Tester",
        "phone_number": "0500000000",
        "home_address": "Haifa",
        "id_number": "ID987"
    }

    # Clean up any existing entry
    db.execute("DELETE FROM Users WHERE UserName = ?", (test_data["username"],), commit=True)

    # Insert the test user - should not insert from here - only from the API
    # this is for example purposes
    db.execute("""
        INSERT INTO Users (
            UserName, FirstName, LastName, PhoneNumber, HomeAddress, ID
        ) VALUES (?, ?, ?, ?, ?, ?)
    """, (
        test_data["username"],
        test_data["first_name"],
        test_data["last_name"],
        test_data["phone_number"],
        test_data["home_address"],
        test_data["id_number"]
    ), commit=True)

    # Fetch inserted user
    result = db.execute("SELECT * FROM Users WHERE UserName = ?", (test_data["username"],), fetchone=True)
    
    # Validate results
    assert result is not None
    assert result["FirstName"] == test_data["first_name"]
    assert result["LastName"] == test_data["last_name"]
    assert result["PhoneNumber"] == test_data["phone_number"]
    assert result["HomeAddress"] == test_data["home_address"]
    assert result["ID"] == test_data["id_number"]