def onCountryPress(country):
    



import sqlite3

# 1. Create or connect to the database
conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()

# 2. Create the table (if it doesn't already exist)
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL
)
''')
conn.commit()

# 3. Insert users into the table
cursor.execute('''
INSERT INTO users (name, email)
VALUES ('John Doe', 'john.doe@example.com')
''')
cursor.execute('''
INSERT INTO users (name, email)
VALUES (?, ?)
''', ('Jane Smith', 'jane.smith@example.com'))
conn.commit()

# 4. Retrieve and display all users
cursor.execute('SELECT * FROM users')
users = cursor.fetchall()
print("Users in the database:")
for user in users:
    print(user)

# 5. Update John's email address
cursor.execute('''
UPDATE users
SET email = ?
WHERE id = ?
''', ('john.newemail@example.com', 1))
conn.commit()

# 6. Delete Jane Smith
cursor.execute('''
DELETE FROM users WHERE id = ?
''', (2,))
conn.commit()

# 7. Display users after update and delete
cursor.execute('SELECT * FROM users')
users = cursor.fetchall()
print("\nUsers after update and delete:")
for user in users:
    print(user)

# 8. Close the connection
conn.close()




