import json
import os
from datetime import datetime

def datetime_serializer(obj):
    if isinstance(obj, datetime):
        return obj.strftime('%Y-%m-%d %H:%M:%S')
    raise TypeError(f'Type {obj.__class__.__name__} not serializable')

# Then when saving sales, use the custom serializer:
def save_sales():
    with open(SALES_FILE, "w") as file:
        json.dump(sales, file, indent=4, default=datetime_serializer)

# File paths
BOARD_GAMES_FILE = "data/board_games_data.json"
SALES_FILE = "data/sales_data.json"
CUSTOMERS_FILE = "data/customers_data.json"
DELIVERY_FILE = "data/delivery_data.json"
DONATIONS_FILE = "data/donations_data.json"

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

if os.path.exists(DELIVERY_FILE):
    with open(DELIVERY_FILE, "r") as file:
        deliveries = json.load(file)
else:
    deliveries = []

if os.path.exists(DONATIONS_FILE):
    with open(DONATIONS_FILE, "r") as file:
        donations = json.load(file)
else:
    donations = []

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

def save_deliveries():
    with open(DELIVERY_FILE, "w") as file:
        json.dump(deliveries, file, indent=4)

def save_donations():
    with open(DONATIONS_FILE, "w") as file:
        json.dump(donations, file, indent=4)

# Function to show available games
def show_board_games():
    print("Available board games:")
    for game in board_games:
        print(f"{game['name']} (${game['price']}) - Stock: {game['stock']}")


# Function to handle customer registration
def register_customer():
    print("Please register by filling in your details.")
    while True:
        username = input("Enter a username (at least 4 characters, no spaces): ")
        if len(username) < 4 or ' ' in username:
            print("Invalid username. Please ensure it is at least 4 characters long and contains no spaces.")
        elif any(c["username"] == username for c in customers):
            print("This username is already taken. Please try a different one.")
        else:
             print("Username saved successfully.")
             break

    while True:
        password = input("Enter a password: ")
        if password.startswith(' '):
            print("Invalid password. Please ensure it does not start with a space.")
        else:
            print("Password saved successfully.")
            break

    while True:
        name = input("Enter your name: ")
        if any(char.isdigit() for char in name):
            print("Name should not contain numbers.")
        elif name.startswith(' '):
            print("Name should not start with a space.")
        elif not name.strip():
            print("Name should contain at least 1 character.")
        else:
            print("Name saved successfully.")
            break

    while True:
        email = input("Enter your email address: ")
        if any(c["email"] == email for c in customers):
            print("This email is already registered. Please use a different email.")
        elif not email.strip():
            print("Email field should not be empty.")
        elif '@' not in email or '.' not in email.split('@')[-1]:
            print("Invalid email. Email must contain '@' and a valid domain (e.g., '.com').")
        else:
            print("Email saved successfully.")
            break

    while True:
        city = input("Enter your city: ")
        if city.startswith(' '):
            print("City should not start with a space.")
        elif not city.strip():
            print("City field should not be empty.")
        else:
            print("City saved successfully.")
            break
    while True:
        try:
            age_input = input("Enter your age: ").strip()
            if not age_input:
                print("Age field should not be empty.")
                continue
            age = int(age_input)
            if age < 16:
                print("You must be at least 16 years old to be registered.")
            else:
                print("Age saved successfully.")
                break
        except ValueError:
            print("Age must be a valid number, not other characters.")

    while True:
        gender = input("Enter your gender (Male/Female): ").strip().capitalize()
        if gender not in ["Male", "Female"]:
            print("Gender should be 'Male' or 'Female'.")
        elif not gender:
            print("Gender field should not be empty.")
        else:
            print("Gender saved successfully.")
            break

    new_customer = {
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


# Function to handle guest behavior
def guest():
    print("Proceeding as a guest. No registration required.")
    return {"username": "guest", "name": "Guest User", "email": "", "city": "", "age": 0, "gender": ""}


# Function to handle customer login
def login_customer():
    while True:
        username = input("Enter your username: ")
        if len(username) < 4 or ' ' in username:
            print("Invalid username. Please ensure it is at least 4 characters long and contains no spaces.")
        elif not any(c["username"] == username for c in customers):
            print("Username not found.")
            choice = input("Would you like to try again, register, or proceed as a guest? (try/register/guest): ").lower()
            if choice == "register":
                return register_customer()
            elif choice == "try":
                continue
            elif choice == "guest":
                return guest()  # Allow the user to proceed as a guest
            else:
                print("Invalid choice. Please try again.")
                continue
        else:
            print("Username entered successfully.")
            break
    while True:
        password = input("Enter your password: ")
        if password.startswith(' '):
            print("Invalid password. Please ensure it does not start with a space.")
        elif not any(c["password"] == password for c in customers if c["username"] == username):
            print("Invalid password. Please try again.")
        else:
            print("Password entered successfully.")
            break

    customer = next((c for c in customers if c["username"] == username and c["password"] == password), None)
    if not customer:
        print("Invalid username or password. If you don't have an account, please register.")
        choice = input("Would you like to register or proceed as a guest? (register/guest): ").lower()
        if choice == "register":
            return register_customer()
        elif choice == "guest":
            return guest()  # Allow the user to proceed as a guest
        else:
            print("Invalid choice. Please try again.")
            return None

    print(f"Welcome back, {customer['name']}!")
    return customer


# Function to display customer's purchase history
def show_purchase_history(username):
    print("Your purchase history:")
    purchases = [sale for sale in sales if sale["username"] == username and sale["username"]!="guest"]
    if not purchases:
        print("You have not purchased any items yet.")
        return
    for purchase in purchases:
        game = next(g for g in board_games if g["gameID"] == purchase["gameID"])
        print(f"- {game['name']} (Quantity: {purchase['quantity']}, Total Price: ${purchase['totalPrice']:.2f}, Date: {purchase['Date']}.)")


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

    while True:  # Repeat until the user answers with 'yes' or 'no'
        agree_delivery = input("Do you agree to pay the delivery fee and proceed with delivery? (yes/no): ").lower()
        if agree_delivery in ["yes"]:
            print("Delivery confirmed. Processing your payment...")
            delivery_info = {
                "deliveryID": f"D{len(deliveries) + 1}",
                "username": customer["username"],
                "deliveryAddress": {"city": city, "street": street, "houseNumber": house_number},
                "deliveryFee": delivery_fee,
                "date": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            deliveries.append(delivery_info)
            save_deliveries()
            return total_with_delivery  # Return updated total amount with delivery fee
        elif agree_delivery in ["no"]:
            print("You chose not to proceed with delivery. Please visit our shop to pick up your order.")
            return total_price  # Return original total amount without delivery fee
        else:
            print("Invalid input. Please answer with 'yes' or 'no'.")  # Ask again if the input is invalid


# Function to process payment
def process_payment(amount, customer):
    while True:  # Loop until a valid input is given
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
                while True:  # Keep asking until a valid response is entered
                    donate = input("Do you really want to donate extra money (yes/no)? ").lower()
                    if donate == "yes":
                        print("Purchase complete. Thank you for your generosity!")
                        donation_info = {
                            "donationID": f"D{len(donations) + 1}",
                            "username": customer["username"],
                            "amount": extra,
                            "date": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        }
                        donations.append(donation_info)
                        save_donations()
                        break  # Exit the loop once donation is processed
                    elif donate == "no":
                        print("Thank you for your payment. The exact amount has been processed.")
                        break  # Exit the loop if the user doesn't want to donate
                    else:
                        print("Invalid input. Please answer with 'yes' or 'no'.")  # Keep prompting until valid response
            else:
                print("Purchase complete.")
            break  # Exit the loop once a valid payment method is processed
        elif payment_method == "cash":
            print("Please pay in cash at the shop.")
            break  # Exit the loop once "cash" is selected
        else:
            print("Invalid input. Please choose either 'card' or 'cash'.")  # Prompt for valid input
    return True

# Function to handle the customer's game selection
def select_games():
    basket = []  # Initialize an empty basket
    while True:
        show_board_games()  # Display available games
        print("*" * 60)
        print("*" * 60)
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
        while True:  # Loop to ask for valid input
            another_game = input("Do you want to add another game to your basket? (yes/no): ").lower()
            if another_game == "yes":
                break  # Exit the loop and continue adding games
            elif another_game == "no":
                break  # Exit the loop and stop adding games
            else:
                print("Invalid input. Please answer with 'yes' or 'no'.")  # Ask again if the input is invalid
        if another_game == "no":
            break  # Exit the loop and finish game selection
    return basket


# Function to calculate the total price of the basket
def calculate_total_price(basket):
    total_price = sum(item["price"] * item["quantity"] for item in basket)
    return total_price

# Function to handle customer purchase
def purchase_game():
    while True:
        action = input("Do you want to log in, register, or proceed as a guest? (log in/register/guest): ").lower()
        try:
            if action == "register":
                customer = register_customer()
            elif action == "log in":
                customer = login_customer()
                if not customer:
                    return  # Exit if login fails or customer doesn't register
            elif action == "guest":
                customer = guest()  # Call guest() function here
            else:
                raise ValueError("Invalid option. Please choose 'log in', 'register', or 'guest'.")
            break
        except ValueError as e:
            print(e)

    # Show purchase history
    if action!="guest" and action!="register" and action=="log in":
        while True:
            view_history = input("Do you want to view your purchase history? (yes/no): ").lower()
            if view_history == "yes":
                print("*" * 60)
                show_purchase_history(customer["username"])
                print("*" * 60)
                print("*" * 60)
                break
            elif view_history == "no":
                break
            else:
                print("Invalid input. Please write 'yes' or 'no'. ")

    # Let the customer select games
    basket = select_games()
    print("*" * 60)
    print("*" * 60)
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
    if process_payment(total_price,customer):
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
                "totalPrice": item["price"] * item["quantity"],
                "city": customer["city"],
                "Date": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            })

        # Save changes to the board games and sales
        save_board_games()
        save_sales()
        print("Thank you for your purchase! Your order has been processed successfully.")
    else:
        print("Payment failed or order was cancelled. Your basket has been cleared, and no stock changes were made.")


# Main program execution
purchase_game()

