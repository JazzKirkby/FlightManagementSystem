#importing sqlite3
import sqlite3

#creating the database
conn = sqlite3.connect('Flight_Management_DB')
print ("Database has been created")

#deleting the tables if they exist
conn.execute("DROP TABLE IF EXISTS Pilots")
conn.execute("DROP TABLE IF EXISTS Destinations")
conn.execute("DROP TABLE IF EXISTS Flights")

#creating tables Pilots, Destinations and Flights
conn.execute("CREATE TABLE Pilots (pilot_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, license_number TEXT UNIQUE NOT NULL)")
print ("Table Pilots created successfully")

conn.execute("CREATE TABLE Destinations (destination_id INTEGER PRIMARY KEY AUTOINCREMENT, city TEXT NOT NULL, country TEXT NOT NULL, airport_code TEXT UNIQUE NOT NULL)")
print ("Table Destinations created successfully")

conn.execute("CREATE TABLE Flights (flight_id INTEGER PRIMARY KEY AUTOINCREMENT, flight_number TEXT UNIQUE NOT NULL, departure_time TEXT NOT NULL, arrival_time TEXT NOT NULL, status TEXT NOT NULL, pilot_id INTEGER, destination_id INTEGER, FOREIGN KEY (pilot_id) REFERENCES Pilots (pilot_id), FOREIGN KEY (destination_id) REFERENCES Destinations (destination_id))")
print ("Table Flights created successfully")
