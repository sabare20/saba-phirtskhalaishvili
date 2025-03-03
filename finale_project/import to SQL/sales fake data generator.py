import json
import random
import os
from datetime import datetime, timedelta

# Define the number of sales to generate
NUM_SALES = 7000

# Define possible values and ranges
CUSTOMER_ID_RANGE = (1, 5000)  # Assuming 6000 unique customers
START_DATE = datetime(2024, 9, 1, 10, 0)  # Start from September 1, 2024, at 10:00 AM
END_DATE = datetime(2025, 2, 28, 22, 0)  # End on February 28, 2025, at 10:00 PM (not 11:00 PM)

# Define game ID distribution with weighted preference
GAME_IDS = [23] * 30 + [22] * 25 + [1] * 20 + [15] * 15 + [12] * 10 + [7] * 8 + [6] * 6 + [2] * 5

# Define quantity distribution (more sales should have quantity 1, then 2, then 3, then 5)
QUANTITIES = [1] * 70 + [2] * 20 + [3] * 10

# Define board games with their prices
GAMES = {
    1: 35, 2: 30, 3: 25, 4: 40, 5: 120, 6: 35, 7: 28, 8: 45, 9: 50, 10: 60,
    11: 55, 12: 30, 13: 70, 14: 35, 15: 20, 16: 18, 17: 70, 18: 25, 19: 65,
    21: 80, 22: 5, 23: 5
}

# Calculate the total time span in seconds
total_time_span = (END_DATE - START_DATE).total_seconds()


# Define a function to generate a timestamp with a trend and spread
def generate_timestamp(sale_id, total_sales, start_date, end_date):
    # Calculate the progress ratio (0 at the start, 1 at the end)
    progress = sale_id / total_sales

    # Apply a non-linear trend (e.g., exponential growth)
    trend_factor = progress ** 2  # Adjust the exponent to control the trend

    # Calculate the timestamp based on the trend
    elapsed_time = total_time_span * trend_factor

    # Add randomness to spread out sales
    random_offset = random.randint(0, int(total_time_span * 0.01))  # Add up to 1% randomness
    elapsed_time += random_offset

    return start_date + timedelta(seconds=elapsed_time)


# Define a function to generate a random time within the allowed range
def generate_random_time():
    # Weighted distribution for peak hours (15:00 to 20:30)
    if random.random() < 0.7:  # 70% chance for the peak window (15:00 to 20:30)
        hour = random.randint(15, 20)
        if hour == 20:
            minute = random.choice([0, 30])  # Limit minute to 00 or 30
        else:
            minute = random.randint(0, 59)
    else:  # 30% chance for other times (10:00 to 14:59 or 20:30 to 22:00)
        hour = random.choice([10, 11, 12, 13, 14, 21, 22])
        minute = random.randint(0, 59)

    # Adjust to ensure we stay within the limits of 10:00 to 22:00
    if hour == 22:
        minute = 0  # Ensure it's exactly 22:00

    second = random.randint(0, 59)
    return hour, minute, second


# Define a function to check if a date is a weekend (Saturday or Sunday)
def is_weekend(date):
    return date.weekday() >= 5  # 5 = Saturday, 6 = Sunday


# Generate sales data
sales_data = []
current_datetime = START_DATE

for sale_id in range(1, NUM_SALES + 1):
    customer_id = random.randint(*CUSTOMER_ID_RANGE)
    game_id = random.choice(GAME_IDS)
    quantity = random.choice(QUANTITIES)
    total_price = GAMES[game_id] * quantity

    # Generate a timestamp with a trend and spread
    current_datetime = generate_timestamp(sale_id, NUM_SALES, START_DATE, END_DATE)

    # Check if the current date is a weekend
    is_weekend_day = is_weekend(current_datetime)

    # Adjust the number of sales on weekends (more frequent sales)
    if is_weekend_day:
        # On weekends, generate more sales by reducing the time gap
        current_datetime += timedelta(seconds=random.randint(60, 1800))  # Add 1 minute to 30 minutes
    else:
        # On weekdays, generate fewer sales by increasing the time gap
        current_datetime += timedelta(seconds=random.randint(1800, 7200))  # Add 30 minutes to 2 hours

    # Generate a random time within the allowed range (10:00 to 22:00), focusing on 15:00 to 20:30
    hour, minute, second = generate_random_time()
    current_datetime = current_datetime.replace(hour=hour, minute=minute, second=second)

    # Ensure the timestamp is within the allowed range (10:00 AM to 10:00 PM)
    if current_datetime.hour < 10:
        current_datetime = current_datetime.replace(hour=10, minute=0, second=0)
    elif current_datetime.hour >= 23:
        current_datetime = current_datetime.replace(hour=22, minute=0, second=0)

    # Ensure the timestamp is strictly increasing
    if sale_id > 1:
        # Combine Date and time for the previous sale
        previous_date_str = sales_data[-1]["Date"] + " " + sales_data[-1]["time"]
        previous_date = datetime.strptime(previous_date_str, "%Y-%m-%d %H:%M:%S")

        # If the current datetime is less than or equal to the previous datetime, adjust it
        if current_datetime <= previous_date:
            current_datetime = previous_date + timedelta(seconds=random.randint(60, 3600))  # Add 1 minute to 1 hour

    # Format the sale date and time as required
    sale_date = current_datetime.strftime("%Y-%m-%d")
    sale_time = current_datetime.strftime("%H:%M:%S")

    # Append the sale data
    sales_data.append({
        "saleID": sale_id,
        "customerID": customer_id,
        "gameID": game_id,
        "quantity": quantity,
        "totalPrice": total_price,
        "Date": sale_date,
        "time": sale_time
    })

# Ensure the "data" directory exists
os.makedirs("data", exist_ok=True)

# Save data to JSON file
with open("data/sales_data.json", "w", encoding="utf-8") as f:
    json.dump(sales_data, f, indent=4)

print("Sales data successfully generated and saved in 'data/sales_data.json'")
