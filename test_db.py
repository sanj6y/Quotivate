import sqlite3

# Connect to the database
conn = sqlite3.connect('user.db')

# Create a cursor
cursor = conn.cursor()

# Select all data from the table and fetch the results
cursor.execute("SELECT * FROM users")
results = cursor.fetchall()

# Print the results
for row in results:
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()
