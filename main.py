#importing sqlite3
import sqlite3

#defining function called main
def main():
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

    #Adding data into Pilots, Destinations and Flights
    pilots = [
        ('12345', 'Harry Kane', '654321'),
        ('12346', 'David Beckham', '345678'),
        ('12347', 'Christiano Ronaldo', '654267'),
        ('12348', 'Lionel Messi', '468368'),
        ('12349', 'Kylian Mbappé', '346851'),
        ('12350', 'Marcus Rashford', '563052')
    ]

    conn.executemany("INSERT INTO Pilots (pilot_id, name, license_number) VALUES (?, ?, ?)", pilots)
    conn.commit()
    print("Records created successfully")
    print("Total number of rows created :", conn.total_changes)

    Destinations = [
        ('54387', 'London', 'United Kingdom', 'LHR'),
        ('54388', 'New York', 'United States', 'JFK'),
        ('54389', 'Los Angeles', 'United States', 'LAX'),
        ('54390', 'Paris', 'France', 'CDG'),
        ('54391', 'Toronto', 'Canada', 'YYZ'),
        ('54392', 'Rome', 'Italy', 'BOM'),
    ]

    conn.executemany("INSERT INTO Destinations (destination_id, city, country, airport_code) VALUES (?, ?, ?, ?)", Destinations)
    conn.commit()
    print("Records created successfully")
    print("Total number of rows created :", conn.total_changes)

    Flights = [
        ('001', '00001', '2025-04-12 08:00', '2025-04-12 17:45', 'On Time', '12345', '54387'),
        ('002', '00002', '2025-04-12 07:30', '2025-04-12 15:35', 'On Time', '12346', '54388'),
        ('003', '00003', '2025-04-12 10:15', '2025-04-12 14:20', 'On Time', '12347', '54389'),
        ('004', '00004', '2025-04-12 09:45', '2025-04-12 10:50', 'On Time', '12348', '54390'),
        ('005', '00005', '2025-04-12 06:50', '2025-04-12 12:10', 'On Time', '12349', '54391'),
        ('006', '00006', '2025-04-12 12:10', '2025-04-12 18:05', 'On Time', '12350', '54392'),
    ]

    conn.executemany("INSERT INTO Flights (flight_id, flight_number, departure_time, arrival_time, status, pilot_id, destination_id) VALUES (?, ?, ?, ?, ?, ?, ?)", Flights)
    conn.commit()
    print("Records created successfully")
    print("Total number of rows created:", conn.total_changes)

#Ensures main only runs if executed directly
if __name__ == "__main__":
    main()
