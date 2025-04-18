# view_update_destination.py

# Here I will define the function called view_update_destination
# and create a cursor object to run the SQL queries
def view_update_destination(conn):
    cursor = conn.cursor()

    # Ask for the destination ID to modify
    destination_id = input("Enter the Destination ID to view and update: ").strip()

    # Query to get the current destination details
    check_query = """
    SELECT destination_id, city, country, airport_code
    FROM Destinations
    WHERE destination_id = ?;
    """
    
    cursor.execute(check_query, (destination_id,))
    destination = cursor.fetchone()

    if destination:
        print(f"Current details for Destination ID {destination_id}:")
        print(f"Destination ID: {destination[0]}, City: {destination[1]}, Country: {destination[2]}, Airport Code: {destination[3]}")

        # Ask for new values (or press Enter to keep the old value)
        city = input(f"Enter new city (current: {destination[1]}): ").strip() or destination[1]
        country = input(f"Enter new country (current: {destination[2]}): ").strip() or destination[2]
        airport_code = input(f"Enter new airport code (current: {destination[3]}): ").strip() or destination[3]

        # Update query to modify the destination details
        update_query = """
        UPDATE Destinations
        SET city = ?, country = ?, airport_code = ?
        WHERE destination_id = ?;
        """

        # Execute the query to update the destination
        cursor.execute(update_query, (city, country, airport_code, destination_id))
        conn.commit()

        # Check if the update was successful
        cursor.execute(check_query, (destination_id,))
        updated_destination = cursor.fetchone()

        if updated_destination:
            print("Destination updated successfully:")
            print(f"Destination ID: {updated_destination[0]}, City: {updated_destination[1]}, Country: {updated_destination[2]}, Airport Code: {updated_destination[3]}")
        else:
            print("Destination not found.")
    else:
        print("Destination not found.")
