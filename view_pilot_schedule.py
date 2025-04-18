# view_pilot_schedule.py

def view_pilot_schedule(conn):
    cursor = conn.cursor()

    # Ask for the pilot's ID
    pilot_id = input("Enter the Pilot ID to view their schedule: ").strip()

    # Query to get the pilot's flight schedule
    query = """
    SELECT f.flight_id, f.departure_time, f.status, d.city
    FROM Flights f
    JOIN Destinations d ON f.destination_id = d.destination_id
    WHERE f.pilot_id = ?;
    """
    
    try:
        # Execute the query with the provided pilot_id
        cursor.execute(query, (pilot_id,))
        
        # Get the results
        pilot_schedule = cursor.fetchall()

        if pilot_schedule:
            print(f"\nSchedule for Pilot ID {pilot_id}:")
            for flight in pilot_schedule:
                print(f"Flight ID: {flight[0]}, Departure Time: {flight[1]}, Status: {flight[2]}, Destination: {flight[3]}")
        else:
            print(f"No flights found for Pilot ID {pilot_id}.")
    
    except Exception as e:
        print(f"Error: {e}")
