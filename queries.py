import sqlite3

# Connect to the database and interact
conn = sqlite3.connect('flight_management.db')
cursor = conn.cursor()

# The SQL query for flight retrieval (you could change the destination, status and departure_date)
query = """
SELECT * 
FROM Flights
WHERE destination = 'New York' 
  AND status = 'On Time'
  AND departure_date >= '2025-04-01';
"""

# Execute the query
cursor.execute(query)

# Fetch and print the results
flights = cursor.fetchall()
for flight in flights:
    print(flight)


















# Commit changes (though for SELECT queries, this isn't necessary)
conn.commit()

cursor.close()
conn.close()
