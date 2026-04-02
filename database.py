import sqlite3
# establish a connection 
conn = sqlite3.connect("data.db")
cursor = conn.cursor()

# creating a table to store the generated data 
cursor.execute("""
CREATE TABLE IF NOT EXISTS readings (
    temp REAL,
    humidity REAL,
    light INTEGER
)
""")

#function to instert the data into the db table 
def save_data(temp, humidity, light):
    cursor.execute(
        "INSERT INTO readings (temp, humidity, light) VALUES (?, ?, ?)",
        (temp, humidity, light)
    )
    conn.commit()
