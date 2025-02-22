import sqlite3

# Connect to SQLite database (it will create the database file if it doesn't exist)
conn = sqlite3.connect('Hotel.db')
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS Hotel (
    Name TEXT,
    Address TEXT,
    mobile_number NUMBER,
    number_days NUMBER,
    room_number NUMBER,
    mode TEXT
)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Table created successfully.")
