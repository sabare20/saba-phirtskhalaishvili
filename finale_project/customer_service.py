import json
import os

# Initialize data from JSON file or use default data if the file does not exist
DATA_FILE = "board_game_shop_data.json"
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as file:
        data = json.load(file)




# Function to save updated data to file
def save_data():
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)
    print("Data has been saved successfully.")


# Function to show available games
def show_board_games():
    print("Available board games:")
    for game in data["boardGames"]:
        print(f"{game['name']} (${game['price']}) - Stock: {game['stock']}")


# Function to handle customer registration
def register_customer():
    print("Please register by filling in your details.")
    username = input("Enter a username: ")
    if any(c["username"] == username for c in data["customers"]):
        print("This username is already taken. Please try a different one.")
        return register_customer()
    password = input("Enter a password: ")
    name = input("Enter your name: ")
    city = input("Enter your city: ")
    new_customer = {"username": username, "password": password, "name": name, "city": city}
    data["customers"].append(new_customer)
    save_data()
    print(f"Registration complete! Welcome, {name}.")
    return new_customer


# Function to handle customer login
def login_customer():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    customer = next((c for c in data["customers"] if c["username"] == username and c["password"] == password), None)
    if not customer:
        print("Invalid username or password. Please try again.")
        return login_customer()
    print(f"Welcome back, {customer['name']}!")
    return customer


# Function to display customer's purchase history
def show_purchase_history(username):
    print("Your purchase history:")
    purchases = [sale for sale in data["sales"] if sale["username"] == username]
    if not purchases:
        print("You have not purchased any items yet.")
        return
    for purchase in purchases:
        game = next(g for g in data["boardGames"] if g["gameID"] == purchase["gameID"])
        print(f"- {game['name']} (Quantity: {purchase['quantity']}, Total Price: ${purchase['totalPrice']:.2f})")


# Function to handle customer purchase
def purchase_game():
    has_account = input("Do you have an account with us? (yes/no): ").lower()

    if has_account == "no":
        customer = register_customer()
    else:
        customer = login_customer()

    # Show purchase history
    view_history = input("Do you want to view your purchase history? (yes/no): ").lower()
    if view_history == "yes":
        show_purchase_history(customer["username"])

    show_board_games()
    game_name = input("Enter the name of the game you want to buy: ")
    quantity = int(input("Enter the quantity: "))
    game = next((g for g in data["boardGames"] if g["name"].lower() == game_name.lower()), None)

    if not game:
        print("Game not found.")
        return

    if game["stock"] < quantity:
        print("Insufficient stock.")
        return

    total_price = game["price"] * quantity
    print(f"Total price: ${total_price:.2f}")

    # Update stock and add to sales
    game["stock"] -= quantity
    data["sales"].append({
        "saleID": f"S{len(data['sales']) + 1}",
        "username": customer["username"],
        "gameID": game["gameID"],
        "quantity": quantity,
        "totalPrice": total_price
    })
    save_data()

    # Ask for delivery or pickup
    delivery_option = input("Do you want delivery (yes/no)? ").lower()
    if delivery_option == "yes":
        handle_delivery(customer)
    else:
        print("Please visit our shop to pick up your order.")

    # Handle payment
    process_payment(total_price)


# Function to handle delivery
def handle_delivery(customer):
    print("Please provide your delivery address details.")
    city = input("Enter your city: ")
    street = input("Enter your street: ")
    house_number = input("Enter your house number: ")

    if city.lower() == "tbilisi":
        print("Your order will be delivered within 3 days.")
    else:
        print("Your order will be delivered within 3-7 days.")


# Function to process payment
def process_payment(amount):
    payment_method = input("How will you pay (card/cash)? ").lower()

    if payment_method == "card":
        card_number = input("Enter your card number: ")
        amount_paid = float(input("Enter the amount to pay: "))

        if amount_paid < amount:
            print("Payment failed: Insufficient amount.")
        elif amount_paid > amount:
            extra = amount_paid - amount
            print(f"The game costs ${amount:.2f}. You are paying an extra ${extra:.2f}.")
            donate = input("Do you really want to donate extra money (yes/no)? ").lower()
            if donate == "yes":
                print("Purchase complete. Thank you for your generosity!")
            else:
                print("Payment canceled.")
        else:
            print("Purchase complete.")
    else:
        print("Please pay in cash at the shop.")


# Main program execution
purchase_game()