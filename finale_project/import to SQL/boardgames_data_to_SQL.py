import json
import pyodbc
import logging

# Set up logging
logging.basicConfig(filename='boardgames_import.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# File path
BOARDGAMES_FILE = "../data/board_games_data.json"

# Load JSON data from file
try:
    with open(BOARDGAMES_FILE, 'r') as file:
        boardgames_data = json.load(file)
    logging.info("JSON file loaded successfully.")
except Exception as e:
    logging.error(f"Error loading JSON file: {e}")
    raise

# Database connection details
SERVER = r'DESKTOP-9N3FCVE\SQLEXPRESS'  # Replace with your server name or IP
DATABASE = 'Boardgames_shop DB'

# Establish the connection
try:
    conn = pyodbc.connect(
        f'DRIVER={{ODBC Driver 17 for SQL Server}};'
        f'SERVER={SERVER};'
        f'DATABASE={DATABASE};'
        f'Trusted_Connection=yes;'
    )
    cursor = conn.cursor()
    logging.info("Database connection established.")
except Exception as e:
    logging.error(f"Error connecting to the database: {e}")
    raise

# Process each boardgame in the JSON data
for boardgame in boardgames_data:
    try:
        # Check if the gameID already exists
        cursor.execute(
            "SELECT game_ID FROM boardgames WHERE game_ID = ?",
            boardgame['gameID']
        )
        if cursor.fetchone():  # If the record exists, update it
            cursor.execute(
                "UPDATE boardgames SET name = ?, price = ?, stock = ?, genre_ID = ? "
                "WHERE game_ID = ?",
                boardgame['name'],
                boardgame['price'],
                boardgame['stock'],
                boardgame['genreID'],
                boardgame['gameID']
            )
            logging.info(f"Updated boardgame: {boardgame['name']} (ID: {boardgame['gameID']})")
        else:  # If the record does not exist, insert it
            cursor.execute(
                "INSERT INTO boardgames (game_ID, name, price, stock, genre_ID) "
                "VALUES (?, ?, ?, ?, ?)",
                boardgame['gameID'],
                boardgame['name'],
                boardgame['price'],
                boardgame['stock'],
                boardgame['genreID']
            )
            logging.info(f"Inserted boardgame: {boardgame['name']} (ID: {boardgame['gameID']})")
    except Exception as e:
        logging.error(f"Error processing boardgame {boardgame.get('name', 'Unknown')}: {e}")

# Commit the transaction
try:
    conn.commit()
    logging.info("Data processed successfully!")
except Exception as e:
    logging.error(f"Error committing transaction: {e}")
    conn.rollback()
finally:
    # Close the connection
    cursor.close()
    conn.close()
    logging.info("Database connection closed.")