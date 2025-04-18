# add_flight.py

# Here I will define the function called add_flight
# and create a cursor object to run the SQL queries
def add_flight(conn):
    cursor = conn.cursor()

    # Collect the input from the user for the new flight
    flight_number = input("Enter Flight Number: ").strip()
    departure_time = input("Enter Departure Time (YYYY-MM-DD HH:MM): ").strip()
    arrival_time = input("Enter Arrival Time (YYYY-MM-DD HH:MM): ").strip()
    status = input("Enter Flight Status (e.g., On Time, Delayed): ").strip().title()
    pilot_id = input("Enter Pilot ID: ").strip()
    destination_id = input("Enter Destination ID: ").strip()

    # Insert the new flight into the Flights table
    query = """
    INSERT INTO Flights (flight_number, departure_time, arrival_time, status, pilot_id, destination_id)
    VALUES (?, ?, ?, ?, ?, ?)
    """
    params = (
        flight_number,
        departure_time,
        arrival_time,
        status,
        pilot_id if pilot_id else None,
        destination_id
    )

    try:
        cursor.execute(query, params)
        conn.commit()
        print("Flight added successfully!")

        # Retrieve and print the newly added flight
        cursor.execute("SELECT * FROM Flights WHERE flight_number = ?", (flight_number,))
        new_flight = cursor.fetchone()
        print("New Flight Details:", new_flight)

    except Exception as e:
        print("Failed to add flight:", e)
