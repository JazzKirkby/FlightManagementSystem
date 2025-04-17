# assign_pilot.py

def assign_pilot(conn):
    cursor = conn.cursor()

    # Ask the user for flight_id and pilot_id
    flight_id = input("Enter the Flight ID to assign a pilot: ").strip()
    pilot_id = input("Enter the Pilot ID to assign to the flight: ").strip()

    try:
        # Check if the pilot_id exists in the Pilots table
        check_pilot_query = """
        SELECT pilot_id
        FROM Pilots
        WHERE pilot_id = ?;
        """
        cursor.execute(check_pilot_query, (pilot_id,))
        pilot_exists = cursor.fetchone()

        if not pilot_exists:
            print(f"Pilot ID {pilot_id} does not exist. Please enter a valid Pilot ID.")
            return

        # Check and print the flight details before the update
        check_query_before = """
        SELECT flight_id, departure_time, status, pilot_id
        FROM Flights
        WHERE flight_id = ?;
        """
        cursor.execute(check_query_before, (flight_id,))
        flight_before = cursor.fetchone()

        if flight_before:
            print("\nBefore the update:")
            print(f"Flight_ID: {flight_before[0]}, Departure Time: {flight_before[1]}, Status: {flight_before[2]}, Pilot ID: {flight_before[3]}")
        else:
            print("Flight not found. Cannot update.")
            return

        # Update the pilot for the given flight
        update_query = """
        UPDATE Flights
        SET pilot_id = ?
        WHERE flight_id = ?;
        """
        cursor.execute(update_query, (pilot_id, flight_id))
        conn.commit()

        # Check if the update was successful and print the updated flight
        check_query_after = """
        SELECT flight_id, departure_time, status, pilot_id
        FROM Flights
        WHERE flight_id = ?;
        """
        cursor.execute(check_query_after, (flight_id,))
        flight_after = cursor.fetchone()

        if flight_after:
            print("\nAfter the update:")
            print(f"Flight_ID: {flight_after[0]}, Departure Time: {flight_after[1]}, Status: {flight_after[2]}, Pilot ID: {flight_after[3]}")
        else:
            print("Flight not found after update.")

    except Exception as e:
        print(f"Error: {e}")
