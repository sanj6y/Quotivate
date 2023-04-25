

import sqlite3
import json

# Connect to the database
conn = sqlite3.connect('example.db')

# Define a cursor to execute SQL queries
cur = conn.cursor()

# Execute a query to retrieve data
cur.execute('SELECT * FROM my_table')

# Create an empty list to store JSONs
json_list = []

# Iterate over the query results
for row in cur.fetchall():
    # Convert each row to a dictionary
    row_dict = {'column1': row[0], 'column2': row[1], ...}

    # Convert the dictionary to a JSON string and add it to the list
    json_list.append(json.dumps(row_dict))

# Close the database connection
conn.close()

# Print the list of JSONs
print(json_list)
