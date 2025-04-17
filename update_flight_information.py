# update_flight_information.py

# Here I will define the function called update_flight_information
# and create a cursor object to run the SQL queries
def update_flight_information(conn):
    cursor = conn.cursor()

    # Ask for the flight ID to modify
    flight_id = input("Enter the Flight ID to modify: ").strip()

    # Query to get the current flight details
    check_query = """
    SELECT flight_id, departure_time, status
    FROM Flights
    WHERE flight_id = ?;
    """
    
    cursor.execute(check_query, (flight_id,))
    flight = cursor.fetchone()

    if flight:
        print(f"Current details for Flight ID {flight_id}:")
        print(f"Flight ID: {flight[0]}, Departure Time: {flight[1]}, Status: {flight[2]}")

        # Ask for new values (or press return to keep the old value)
        departure_time = input(f"Enter new departure time (current: {flight[1]}): ").strip() or flight[1]
        status = input(f"Enter new status (current: {flight[2]}): ").strip().title() or flight[2]

        # Update query to modify the flight details
        update_query = """
        UPDATE Flights
        SET departure_time = ?, status = ?
        WHERE flight_id = ?;
        """

        # Execute the query to update the flight
        cursor.execute(update_query, (departure_time, status, flight_id))
        conn.commit()

        # Check if the update was successful
        cursor.execute(check_query, (flight_id,))
        updated_flight = cursor.fetchone()

        if updated_flight:
            print("Flight updated successfully:")
            print(f"Flight ID: {updated_flight[0]}, Departure Time: {updated_flight[1]}, Status: {updated_flight[2]}")
        else:
            print("Flight not found.")
    else:
        print("Flight not found.")
