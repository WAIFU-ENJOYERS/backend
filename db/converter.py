import psycopg2
import json

# Edit database configuration here
DATABASE_HOST_NAME = "127.0.0.1"
DATABASE_NAME = "waifu-db"
DATABASE_USERNAME = "root"
DATABASE_PASSWORD = "root"

# Connect to the database
conn = psycopg2.connect(
    host=DATABASE_HOST_NAME,
    database=DATABASE_NAME,
    user=DATABASE_USERNAME,
    password=DATABASE_PASSWORD
)

# Open a cursor to execute queries
cur = conn.cursor()

# Read the JSON data from a file
with open('data.json') as f:
    data = json.load(f)

# Loop through the data and insert each record into the database
for record in data:
    cur.execute("INSERT INTO mytable (column1, column2, column3) VALUES (%s, %s, %s)", (record['column1'], record['column2'], record['column3']))

# Commit the changes and close the connection
conn.commit()
cur.close()
conn.close()
