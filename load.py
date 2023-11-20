import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('destination_db.db')

# Write the transformed data to the database
source_data.to_sql('destination_table', conn, index=False, if_exists='replace')

# Close the database connection
conn.close()
