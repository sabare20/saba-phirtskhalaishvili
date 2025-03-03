import json
import pyodbc

# File path
CUSTOMERS_FILE = "../data/customers_data.json"

# Load JSON data from file
with open(CUSTOMERS_FILE, 'r') as file:
    customers_data = json.load(file)

# Step 2: Set up SQL Server connection
server = r'DESKTOP-9N3FCVE\SQLEXPRESS'  # Replace with your server name or IP
database = 'Boardgames_shop DB'

# Establish the connection
conn = pyodbc.connect(
    f'DRIVER={{ODBC Driver 17 for SQL Server}};'
    f'SERVER={server};'
    f'DATABASE={database};'
    f'Trusted_Connection=yes;'
)
cursor = conn.cursor()

# Step 3: Insert JSON data into the SQL Server table
for customer in customers_data:
    try:
        cursor.execute(
            "INSERT INTO customers (username, password, name, email, city, age, gender) "
            "VALUES (?, ?, ?, ?, ?, ?, ?)",
            customer['username'], customer['password'], customer['name'],
            customer['email'], customer['city'], customer['age'], customer['gender']
        )
    except Exception as e:
        print(f"Error inserting customer {customer['username']}: {e}")

# Step 4: Commit the transaction
conn.commit()
print("Data inserted successfully!")

# Step 5: Close the connection
cursor.close()
conn.close()