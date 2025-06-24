#!/usr/bin/env python
import sqlite3
import os

# Always relative to the script location
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_dir = os.path.join(BASE_DIR, "database")

# Create the database folder if it doesn't exist
os.makedirs(db_dir, exist_ok=True)

# Path to the SQLite file
db_path = os.path.join(db_dir, "SSMD.db")

# SQL schema to create all 3 tables
schema = """
CREATE TABLE IF NOT EXISTS Users (
    UserID INTEGER PRIMARY KEY AUTOINCREMENT,
    UserName TEXT NOT NULL,
    CreatedDate TIMESTAMP,
    FirstName TEXT NOT NULL,
    LastName TEXT NOT NULL,
    PhoneNumber TEXT NOT NULL,
    HomeAddress TEXT NOT NULL,
    ID TEXT NOT NULL,
    Email TEXT
);

CREATE TABLE IF NOT EXISTS Patients (
    PatientID INTEGER PRIMARY KEY AUTOINCREMENT,
    FirstName TEXT NOT NULL,
    LastName TEXT NOT NULL,
    ID BIGINT NOT NULL,
    DateOfBirth TIMESTAMP,
    Gender TEXT,
    MedicalHistory TEXT,
    HomeAddress TEXT,
    InterfaceLanguage TEXT
);

CREATE TABLE IF NOT EXISTS Sessions (
    SessionID INTEGER PRIMARY KEY AUTOINCREMENT,
    PatientID INTEGER,
    StartDate TIMESTAMP,
    EndDate TIMESTAMP,
    Summary TEXT,
    TherapistID INTEGER 
);
"""

# Create and initialize the DB
conn = sqlite3.connect(db_path)
cursor = conn.cursor()
cursor.executescript(schema)
conn.commit()
conn.close()

print("✅ Database and tables created at:", db_path)