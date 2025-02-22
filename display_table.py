import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('Hotel.db')
cursor = conn.cursor()

# Fetch all records from the Hotel table
cursor.execute("SELECT * FROM Hotel")
records = cursor.fetchall()

# Check if there are records in the table
if records:
    print("Records in the Hotel table:")
    print("{:<30} {:<50} {:<15} {:<15} {:<15} {:<10}".format("Name", "Address", "Mobile Number", "Number of Days", "Room Number", "Mode"))
    print("=" * 120)  # Print a separator line

    # Loop through the records and display them
    for record in records:
        print("{:<30} {:<50} {:<15} {:<15} {:<15} {:<10}".format(*record))
else:
    print("No records found in the Hotel table.")

# Close the database connection
conn.close()
