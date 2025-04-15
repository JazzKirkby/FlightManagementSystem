# flight_retrieval.py

# Here I will define the function called flight_retrieval 
# and create a cursor object to run the SQL queries
def flight_retrieval(conn):
    cursor = conn.cursor()

# User input section
    airport_code = input("Enter Airport Code (or press return to skip): ").strip().upper()
    status = input("Enter Flight Status (or press return to skip): ").strip().title()
    departure_date = input("Enter Departure Date (YYYY-MM-DD) (or press return to skip): ").strip()

# Query that will gather information from all of the tables
    query = """
    SELECT Flights.flight_number, Flights.departure_time, Flights.arrival_time,
           Flights.status, Pilots.name, Destinations.city, Destinations.airport_code
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

# This is where the query with the params is run
# and then gets all the rows returned by the query and prints them, 
# or tells you there was nothing found
    cursor.execute(query, params)
    results = cursor.fetchall()

    if results:
        for row in results:
            print(row)
    else:
        print("No matching flights found.")

