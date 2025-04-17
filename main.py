# Importing sqlite3
import sqlite3

# Importing my modules for database manipulation
from view_flights import view_flights
from assign_pilot import assign_pilot
from add_flight import add_flight
from update_flight_information import update_flight_information
from view_update_destination import view_update_destination
from view_pilot_schedule import view_pilot_schedule

# Defining function called main
def main():
    #Creating the database
    conn = sqlite3.connect('Flight_Management_DB')
    cursor = conn.cursor()
    print ("Database has been created")

    # Deleting the tables if they exist
    conn.execute("DROP TABLE IF EXISTS Pilots")
    conn.execute("DROP TABLE IF EXISTS Destinations")
    conn.execute("DROP TABLE IF EXISTS Flights")

    # Creating tables Pilots, Destinations and Flights
    conn.execute("CREATE TABLE Pilots (pilot_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, license_number TEXT UNIQUE NOT NULL)")
    print ("Table Pilots created successfully")

    conn.execute("CREATE TABLE Destinations (destination_id INTEGER PRIMARY KEY AUTOINCREMENT, city TEXT NOT NULL, country TEXT NOT NULL, airport_code TEXT UNIQUE NOT NULL)")
    print ("Table Destinations created successfully")

    conn.execute("CREATE TABLE Flights (flight_id INTEGER PRIMARY KEY AUTOINCREMENT, flight_number TEXT UNIQUE NOT NULL, departure_time TEXT NOT NULL, arrival_time TEXT NOT NULL, status TEXT NOT NULL, pilot_id INTEGER, destination_id INTEGER, FOREIGN KEY (pilot_id) REFERENCES Pilots (pilot_id), FOREIGN KEY (destination_id) REFERENCES Destinations (destination_id))")
    print ("Table Flights created successfully")

    # Adding data into Pilots, Destinations and Flights
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

    # # The SQL query for flight retrieval (you could change the destination, status, and departure_date)
    # query = """
    # SELECT f.departure_time, f.status, d.airport_code 
    # FROM Flights f
    # JOIN Destinations d ON f.destination_id = d.destination_id
    # WHERE d.airport_code = 'JFK'
    #     AND f.status = 'Delayed'
    #     AND f.departure_time >= '2025-04-12 07:30';
    # """

    # # Execute the query and fetch the results
    # cursor.execute(query)
    # flights = cursor.fetchall()

    # # Check if any flights were found and print them, or if not print the else
    # if flights:
    #     for flight in flights:
    #         print(flight)
    # else:
    #     print('No flights identified')

    # # Define the SQL query for schedule modification
    # query = """
    # UPDATE Flights
    # SET departure_time = '2025-04-20 15:30:00', status = 'Delayed'
    # WHERE flight_id = 001;
    # """

    # # Execute the query and commit
    # cursor.execute(query)
    # conn.commit()

    # # I wanted to confirm the changes had been made, so printed them
    # check_query = """
    # SELECT flight_id, departure_time, status
    # FROM Flights
    # WHERE flight_id = 001;
    # """

    # cursor.execute(check_query)
    # updated_flight = cursor.fetchone()

    # if updated_flight:
    #     print("Flight updated successfully:")
    #     print(updated_flight)
    # else:
    #     print("Flight not found.")

    # # Assign the pilot to another flight
    # update_query = """
    # UPDATE Flights
    # SET pilot_id = 12346
    # WHERE flight_id = 002;
    # """
    # cursor.execute(update_query)
    # conn.commit()

    # # Get and print the updated flight with the new pilot
    # check_query = """
    # SELECT flight_id, departure_time, status, pilot_id
    # FROM Flights
    # WHERE flight_id = 002;
    # """
    # cursor.execute(check_query)
    # updated_flight = cursor.fetchone()

    # if updated_flight:
    #     print(f"Updated Flight - Flight_ID: {updated_flight[0]}, Departure Time: {updated_flight[1]}, Status: {updated_flight[2]}, Pilot ID: {updated_flight[3]}")
    # else:
    #     print("Flight not found.")














    # while True:
    #     print("\nWhat would you like to do?")
    #     print("1. Add a New Flight")
    #     print("2. View Flights by Criteria")
    #     print("3. Update Flight Information")
    #     print("4. Assign Pilot to Flight")
    #     print("5. View Pilot Schedule")
    #     print("6. View/Update Destination Information")
    #     print("7. Exit")

    #     choice = input("Enter your choice (1-7): ")

    #     if choice == '1':
    #         add_flight(conn)
    #     elif choice == '2':
    #         view_flights(conn)
    #     elif choice == '3':
    #         update_flight_information(conn)
    #     elif choice == '4':
    #         assign_pilot(conn)
    #     elif choice == '5':
    #         view_pilot_schedule(conn)
    #     elif choice == '6':
    #         view_update_destination(conn)
    #     elif choice == '7':
    #         print("Exiting...")
    #         break
    #     else:
    #         print("Invalid choice. Try again.")

    # Close the database connection
    # conn.close()
    # cursor.close()
    
# Ensures main only runs if executed directly
if __name__ == "__main__":
    main()