import json
import os

# File paths
BOARD_GAMES_FILE = "board_games_data.json"
SALES_FILE = "sales_data.json"
CUSTOMERS_FILE = "customers_data.json"

# Load or initialize data
if os.path.exists(BOARD_GAMES_FILE):
    with open(BOARD_GAMES_FILE, "r") as file:
        board_games = json.load(file)
else:
    board_games = []

if os.path.exists(SALES_FILE):
    with open(SALES_FILE, "r") as file:
        sales = json.load(file)
else:
    sales = []

if os.path.exists(CUSTOMERS_FILE):
    with open(CUSTOMERS_FILE, "r") as file:
        customers = json.load(file)
else:
    customers = []


# Save data functions
def save_board_games():
    with open(BOARD_GAMES_FILE, "w") as file:
        json.dump(board_games, file, indent=4)


def save_sales():
    with open(SALES_FILE, "w") as file:
        json.dump(sales, file, indent=4)


def save_customers():
    with open(CUSTOMERS_FILE, "w") as file:
        json.dump(customers, file, indent=4)


# Function to show available games
def show_board_games():
    print("Available board games:")
    for game in board_games:
        print(f"{game['name']} (${game['price']}) - Stock: {game['stock']}")


# Function to handle customer registration
def register_customer():
    print("Please register by filling in your details.")
    username = input("Enter a username: ")
    if any(c["username"] == username for c in customers):
        print("This username is already taken. Please try a different one.")
        return register_customer()

    password = input("Enter a password: ")
    name = input("Enter your name: ")
    email = input("Enter your email address: ")
    if any(c["email"] == email for c in customers):
        print("This email is already registered. Please use a different email.")
        return register_customer()

    city = input("Enter your city: ")
    age = int(input("Enter your age: "))
    gender = input("Enter your gender (Male/Female): ")

    # Automatically generate a unique customer ID
    customer_id = f"C{len(customers) + 1}"  # Format as CUST0001, CUST0002, etc.

    new_customer = {
        "customerID": customer_id,
        "username": username,
        "password": password,
        "name": name,
        "email": email,
        "city": city,
        "age": age,
        "gender": gender
    }
    customers.append(new_customer)
    save_customers()
    print(f"Registration complete! Welcome, {name}.")
    return new_customer


# Function to handle customer login
def login_customer():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    customer = next((c for c in customers if c["username"] == username and c["password"] == password), None)
    if not customer:
        print("Invalid username or password. If you don't have an account, please register.")
        choice = input("Would you like to register? (yes/no): ").lower()
        if choice == "yes":
            return register_customer()
        else:
            print("You must have an account to make purchases.")
            return None
    print(f"Welcome back, {customer['name']}!")
    return customer


# Function to display customer's purchase history
def show_purchase_history(username):
    print("Your purchase history:")
    purchases = [sale for sale in sales if sale["username"] == username]
    if not purchases:
        print("You have not purchased any items yet.")
        return
    for purchase in purchases:
        game = next(g for g in board_games if g["gameID"] == purchase["gameID"])
        print(f"- {game['name']} (Quantity: {purchase['quantity']}, Total Price: ${purchase['totalPrice']:.2f})")


# Function to handle delivery
def handle_delivery(customer, total_price):
    print("Please provide your delivery address details.")
    city = input("Enter your city: ")
    street = input("Enter your street: ")
    house_number = input("Enter your house number: ")

    if city.lower() == "tbilisi":
        delivery_fee = 2.0
        print("Delivery fee for Tbilisi: $2.00")
        print("Your order will be delivered within 3 days.")
    else:
        delivery_fee = 7.0
        print("Delivery fee for locations outside Tbilisi: $7.00")
        print("Your order will be delivered within 3-7 days.")

    total_with_delivery = total_price + delivery_fee
    print(f"The total amount with delivery is: ${total_with_delivery:.2f}")

    agree_delivery = input("Do you agree to pay the delivery fee and proceed with delivery? (yes/no): ").lower()
    if agree_delivery == "yes":
        print("Delivery confirmed. Processing your payment...")
        return total_with_delivery  # Return updated total amount with delivery fee
    else:
        print("You chose not to proceed with delivery. Please visit our shop to pick up your order.")
        return total_price  # Return original total amount without delivery fee


# Function to process payment
def process_payment(amount):
    payment_method = input("How will you pay (card/cash)? ").lower()

    if payment_method == "card":
        while True:
            card_number = input("Enter your card number: ")
            if card_number.isdigit() and len(card_number) == 8:
                break
            else:
                print("Invalid input. Please enter an 8-digit number.")
        while True:
            try:
                amount_paid = float(input("Enter the amount to pay: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        if amount_paid < amount:
            print("Payment failed: Insufficient amount.")
            return False
        elif amount_paid > amount:
            extra = amount_paid - amount
            print(f"The game costs ${amount:.2f}. You are paying an extra ${extra:.2f}.")
            donate = input("Do you really want to donate extra money (yes/no)? ").lower()
            if donate == "yes":
                print("Purchase complete. Thank you for your generosity!")
            else:
                print("Thank you for your payment. The exact amount has been processed.")
        else:
            print("Purchase complete.")
    else:
        print("Please pay in cash at the shop.")
    return True

# Function to handle the customer's game selection
def select_games():
    basket = []  # Initialize an empty basket
    while True:
        show_board_games()  # Display available games
        game_name = input("Enter the name of the game you want to add to your basket: ")
        quantity = int(input("Enter the quantity: "))
        game = next((g for g in board_games if g["name"].lower() == game_name.lower()), None)

        if not game:
            print("Game not found. Please choose a valid game.")
            continue

        if game["stock"] < quantity:
            print(f"Insufficient stock. Only {game['stock']} available.")
            continue

        # Add the selected game to the basket
        basket.append({"gameID": game["gameID"], "name": game["name"], "quantity": quantity, "price": game["price"]})
        print(f"{quantity} x {game['name']} has been added to your basket.")

        # Ask if the customer wants to add more games
        another_game = input("Do you want to add another game to your basket? (yes/no): ").lower()
        if another_game != "yes":
            break

    return basket


# Function to calculate the total price of the basket
def calculate_total_price(basket):
    total_price = sum(item["price"] * item["quantity"] for item in basket)
    return total_price


# Function to handle customer purchase
def purchase_game():
    action = input("Do you want to log in or register? (log in/register): ").lower()

    if action == "register":
        customer = register_customer()
    elif action == "log in":
        customer = login_customer()
        if not customer:
            return  # Exit if login fails or customer doesn't register
    else:
        print("Invalid option. Please choose 'log in' or 'register'.")
        return

    # Show purchase history
    view_history = input("Do you want to view your purchase history? (yes/no): ").lower()
    if view_history == "yes":
        show_purchase_history(customer["username"])

    # Let the customer select games
    basket = select_games()

    if not basket:
        print("Your basket is empty. No purchase made.")
        return

    # Calculate total price
    total_price = calculate_total_price(basket)
    print(f"The total price for your basket is: ${total_price:.2f}")

    # Ask for delivery or pickup
    delivery_option = input("Do you want delivery (yes/no)? ").lower()
    if delivery_option == "yes":
        total_price = handle_delivery(customer, total_price)
    else:
        print("Please visit our shop to pick up your order.")

    # Confirm payment
    if process_payment(total_price):
        # If payment is successful, update stock and save the sale
        for item in basket:
            game = next(g for g in board_games if g["gameID"] == item["gameID"])
            game["stock"] -= item["quantity"]

            # Add the sale to the sales list
            sales.append({
                "saleID": f"S{len(sales) + 1}",
                "username": customer["username"],
                "gameID": item["gameID"],
                "quantity": item["quantity"],
                "totalPrice": item["price"] * item["quantity"]
            })

        # Save changes to the board games and sales
        save_board_games()
        save_sales()
        print("Thank you for your purchase! Your order has been processed successfully.")
    else:
        print("Payment failed or order was cancelled. Your basket has been cleared, and no stock changes were made.")


# Main program execution
purchase_game()


# Main program execution
purchase_game()
