import json
import pyodbc
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# File path
SALES_FILE = "../data/sales_data.json"

# Load JSON data from file
try:
    with open(SALES_FILE, 'r') as file:
        sales_data = json.load(file)
    logging.info("JSON data loaded successfully.")
except Exception as e:
    logging.error(f"Error loading JSON data: {e}")
    raise

# Database connection details
server = r'DESKTOP-9N3FCVE\SQLEXPRESS'  # Replace with your server name or IP
database = 'Boardgames_shop DB'

# Establish the connection
try:
    conn = pyodbc.connect(
        f'DRIVER={{ODBC Driver 17 for SQL Server}};'
        f'SERVER={server};'
        f'DATABASE={database};'
        f'Trusted_Connection=yes;'
    )
    cursor = conn.cursor()
    logging.info("Database connection established successfully.")
except Exception as e:
    logging.error(f"Error connecting to the database: {e}")
    raise

# Enable IDENTITY_INSERT
cursor.execute("SET IDENTITY_INSERT sales ON")

# Insert JSON data into the SQL Server table
for sale in sales_data:
    try:
        cursor.execute(
            "INSERT INTO sales (sale_ID, customer_ID, game_ID, quantity, totalPrice, Date, time) "
            "VALUES (?, ?, ?, ?, ?, ?, ?)",
            sale['saleID'],
            sale['customerID'],
            sale['gameID'],
            sale['quantity'],
            sale['totalPrice'],
            sale['Date'],
            sale['time']
        )
        logging.info(f"Inserted sale ID {sale['saleID']} successfully.")
    except Exception as e:
        logging.error(f"Error inserting sale {sale['saleID']}: {e}")

# Disable IDENTITY_INSERT
cursor.execute("SET IDENTITY_INSERT sales OFF")

# Commit the transaction
try:
    conn.commit()
    logging.info("Data inserted successfully!")
except Exception as e:
    logging.error(f"Error committing transaction: {e}")
    conn.rollback()
finally:
    # Close the connection
    cursor.close()
    conn.close()
    logging.info("Database connection closed.")