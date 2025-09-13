import sqlite3

# Connect to the database
conn = sqlite3.connect('donation.db')
cursor = conn.cursor()

# Check tables in the database
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print("Tables:", cursor.fetchall())

# View donors
cursor.execute("SELECT * FROM donor;")
print("Donors:", cursor.fetchall())

# View recipients
cursor.execute("SELECT * FROM recipient;")
print("Recipients:", cursor.fetchall())

conn.close()