import psycopg2
import json

# Edit database configuration here
DATABASE_HOST_NAME = "127.0.0.1"
DATABASE_NAME = "waifu-db"
DATABASE_USERNAME = "root"
DATABASE_PASSWORD = "root"

# Insert json file of scores here
SCORE_JSON = ""

# Connect to the database
conn = psycopg2.connect(
    host=DATABASE_HOST_NAME,
    database=DATABASE_NAME,
    user=DATABASE_USERNAME,
    password=DATABASE_PASSWORD
)

# Open a cursor to execute queries
cur = conn.cursor()

# Create table
cur.execute(
    """CREATE TABLE IF NOT EXISTS score_table (
  score_id SERIAL PRIMARY KEY,
  points INTEGER NOT NULL,
"""
)

conn.commit()

# Read the JSON data from a file
with open(SCORE_JSON) as f:
    data = json.load(f)


# Loop through the data and insert each record into the database
for record in data:
    cur.execute("INSERT INTO score_table (points) VALUES (%s)", (record['points']))

# Commit the changes and close the connection
conn.commit()
cur.close()
conn.close()
