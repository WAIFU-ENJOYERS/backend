import psycopg2
import json

# Edit database configuration here
DATABASE_HOST_NAME = "127.0.0.1"
DATABASE_NAME = "waifu-db"
DATABASE_USERNAME = "root"
DATABASE_PASSWORD = "root"

WAIFU_JSON = "db/waifus.json"

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
    """CREATE TABLE IF NOT EXISTS waifu_table (
  waifu_id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  likes INTEGER NOT NULL,
  display_picture TEXT NOT NULL);
"""
)

# Read the JSON data from a file
with open(WAIFU_JSON) as f:
    data = json.load(f)


# Loop through the data and insert each record into the database
for record in data:
    cur.execute("INSERT INTO waifu_table (name, likes, display_picture) VALUES (%s, %s, %s)", (record['name'], record['likes'], record['display_picture']))

# Commit the changes and close the connection
conn.commit()
cur.close()
conn.close()
