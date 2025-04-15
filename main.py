#importing sqlite3
import sqlite3

from flight_retrieval import flight_retrieval

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
        ('12350', 'Marcus Rashford', '563052'),
        ('12351', 'Neymar Jr.', '238563'),
        ('12352', 'Mohamed Salah', '984654'),
        ('12353', 'Robert Lewandowski', '567839'),
        ('12354', 'Sergio Ramos', '345791'),
        ('12355', 'Kevin De Bruyne', '239406'),
        ('12356', 'Gareth Bale', '402953'),
        ('12357', 'Eden Hazard', '374201'),
        ('12358', 'Virgil van Dijk', '809472'),
        ('12359', 'Sadio Mane', '984220')
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
        ('54392', 'Rome', 'Italy', 'FCO'),
        ('54393', 'Berlin', 'Germany', 'TXL'),
        ('54394', 'Madrid', 'Spain', 'MAD'),
        ('54395', 'Dubai', 'United Arab Emirates', 'DXB'),
        ('54396', 'Sydney', 'Australia', 'SYD'),
        ('54397', 'Tokyo', 'Japan', 'HND'),
        ('54398', 'Amsterdam', 'Netherlands', 'AMS'),
        ('54399', 'Bangkok', 'Thailand', 'BKK'),
        ('54400', 'Cape Town', 'South Africa', 'CPT'),
        ('54401', 'Moscow', 'Russia', 'SVO')
    ]
    conn.executemany("INSERT INTO Destinations (destination_id, city, country, airport_code) VALUES (?, ?, ?, ?)", Destinations)
    conn.commit()
    print("Records created successfully")
    print("Total number of rows created :", conn.total_changes)

    Flights = [
        ('001', '00001', '2025-04-12 08:00', '2025-04-12 17:45', 'On Time', '12345', '54387'),
        ('002', '00002', '2025-04-12 07:30', '2025-04-12 15:35', 'Delayed', '12346', '54388'),
        ('003', '00003', '2025-04-12 10:15', '2025-04-12 14:20', 'On Time', '12347', '54389'),
        ('004', '00004', '2025-04-12 09:45', '2025-04-12 10:50', 'On Time', '12348', '54390'),
        ('005', '00005', '2025-04-12 06:50', '2025-04-12 12:10', 'Delayed', '12349', '54391'),
        ('006', '00006', '2025-04-12 12:10', '2025-04-12 18:05', 'On Time', '12350', '54392'),
        ('007', '00007', '2025-04-12 11:00', '2025-04-12 19:20', 'Delayed', '12351', '54393'),
        ('008', '00008', '2025-04-12 13:30', '2025-04-12 22:00', 'On Time', '12352', '54394'),
        ('009', '00009', '2025-04-12 15:00', '2025-04-12 23:50', 'On Time', '12353', '54395'),
        ('010', '00010', '2025-04-12 17:00', '2025-04-12 02:15', 'Delayed', '12354', '54396'),
        ('011', '00011', '2025-04-12 18:30', '2025-04-12 08:10', 'Delayed', '12355', '54397'),
        ('012', '00012', '2025-04-12 20:00', '2025-04-13 06:00', 'On Time', '12356', '54398'),
        ('013', '00013', '2025-04-12 09:00', '2025-04-12 17:15', 'Delayed', '12357', '54399'),
        ('014', '00014', '2025-04-12 12:00', '2025-04-12 21:00', 'On Time', '12358', '54400'),
        ('015', '00015', '2025-04-12 14:45', '2025-04-12 23:30', 'Delayed', '12359', '54401')
    ]


    conn.executemany("INSERT INTO Flights (flight_id, flight_number, departure_time, arrival_time, status, pilot_id, destination_id) VALUES (?, ?, ?, ?, ?, ?, ?)", Flights)
    conn.commit()
    print("Records created successfully")
    print("Total number of rows created:", conn.total_changes)


    flight_retrieval(conn)

    conn.close()

#Ensures main only runs if executed directly
if __name__ == "__main__":
    main()