import sqlite3

# Step 1: Connect to SQLite database (creates a new file 'users.db' if not exists)
conn = sqlite3.connect('users.db')

# Step 2: Create a cursor object to interact with the database
cursor = conn.cursor()

# Step 3: Create a table named 'users' if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
''')

# Step 4: Insert some sample data (optional)
cursor.execute('''
    INSERT INTO users (username, password) VALUES
    ('admin', 'password'),
    ('lewis107', 'watson')
''')

#Ask for login details
USER = str(input('Username: '))
PASS = str(input('Password: '))

# Step 5: Query all users
cursor.execute(f"SELECT * FROM users WHERE username = '{USER}' AND password = '{PASS}'")
print('SELECT * FROM users WHERE username = ? AND password = ?',(USER,PASS))
user = cursor.fetchone()

# Step 6: Print the results
try:
    print(user)
except:
    print('SQL Error')
# Step 7: Commit the transaction and close the connection
conn.commit()
conn.close()
