#!/usr/bin/env python
import sqlite3
import os

# Define path to the local database folder
db_dir = os.path.join(os.getcwd(), 'database')
os.makedirs(db_dir, exist_ok=True)
db_path = os.path.join(db_dir, 'SSMD.db')

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