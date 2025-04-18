# view_flights.py

# Here I will define the function called view_flights
# and create a cursor object to run the SQL queries
def view_flights(conn):
    cursor = conn.cursor()

# User input section (some I have amended to correct to upper case or upper case the first letters)
    airport_code = input("Enter Airport Code (or press return to skip): ").strip().upper()
    status = input("Enter Flight Status (or press return to skip): ").strip().title()
    departure_date = input("Enter Departure Date (YYYY-MM-DD) (or press return to skip): ").strip()
    destination_city = input("Enter Destination City (or press return to skip): ").strip().title()
    pilot_name = input("Enter Pilot Name (or press return to skip): ").strip().title()

# Query that will gather information from Flights and Destinations
# Where 1=1 means I can make more flexible queries and add any number of and conditions
    query = """
    SELECT Flights.flight_number, Flights.departure_time, Flights.arrival_time, Flights.status,
           Pilots.name AS pilot_name, Destinations.city AS destination_city, Destinations.airport_code
    FROM Flights
    JOIN Pilots ON Flights.pilot_id = Pilots.pilot_id
    JOIN Destinations ON Flights.destination_id = Destinations.destination_id
    WHERE 1=1
    """

# This holds the values to put into the query
    params = []

# If the user added an airport code, status or departure date, we 
# can add this to the query and save the value to params
    if airport_code:
        query += " AND Destinations.airport_code = ?"
        params.append(airport_code)
    if status:
        query += " AND Flights.status = ?"
        params.append(status)
    if departure_date:
        query += " AND date(Flights.departure_time) = ?"
        params.append(departure_date)
    if destination_city:
        query += " AND Destinations.city = ?"
        params.append(destination_city)
    if pilot_name:
        query += " AND Pilots.name = ?"
        params.append(pilot_name)

# This is where the query with the params is run
# and then gets all the rows returned by the query and prints them, 
# or tells you there was nothing found
    cursor.execute(query, params)
    results = cursor.fetchall()

    if results:
        for row in results:
            print(f"Flight: {row[0]}, Departure: {row[1]}, Arrival: {row[2]}, Status: {row[3]}, Pilot: {row[4]}, Destination: {row[5]} ({row[6]})")

    else:
        print("No matching flights found.")
