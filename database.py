import sqlite3

conn = sqlite3.connect("data.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS readings (
    temp REAL,
    humidity REAL,
    light INTEGER
)
""")

def save_data(temp, humidity, light):
    cursor.execute(
        "INSERT INTO readings (temp, humidity, light) VALUES (?, ?, ?)",
        (temp, humidity, light)
    )
    conn.commit()
