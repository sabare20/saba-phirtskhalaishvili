import json
import os
from analytics_functions import main_analytics_function

board_game_file = "C:/Users/phirt/OneDrive/სამუშაო დაფა/python.tbc/finale_project/data/board_games_data.json" #r"/finale_project/data/board_games_data.json"
sales_file = "C:/Users/phirt/OneDrive/სამუშაო დაფა/python.tbc/finale_project/data/sales_data.json" #r"/finale_project/data/sales_data.json"
customers_file = "C:/Users/phirt/OneDrive/სამუშაო დაფა/python.tbc/finale_project/data/customers_data.json" #r"/finale_project/data/customers_data.json"
admins_file = "C:/Users/phirt/OneDrive/სამუშაო დაფა/python.tbc/finale_project/data/admins_data.json"  #r"C:\Users\HOME\PycharmProjects\saba-phirtskhalaishvili\finale_project\data\admins_data.json"

if os.path.exists(admins_file):
    with open(admins_file, "r") as file:
        admins = json.load(file)
else:
    admins = []

if os.path.exists(customers_file):
    with open(customers_file, "r") as file:
        customers = json.load(file)
else:
    customers = []


def customers_list():
    customer_list = []
    for game in board_games:
        customer_list.append(game['name'].lower())
    return customer_list


if os.path.exists(board_game_file):
    with open(board_game_file, "r") as file:
        board_games = json.load(file)
else:
    board_games = []


def show_board_games():
    print("Available board games:")
    for game in board_games:
        print(f"{game['name']} (${game['price']}) - Stock: {game['stock']}")


def board_games_list():
    board_game_list = []
    for game in board_games:
        board_game_list.append(game['name'].lower())
    return board_game_list 


def save_updated_stock():
    with open(board_game_file, "w") as file:
        json.dump(board_games, file, indent=4)


def admins_list():
    admin_list = []
    for admin in admins:
        admin_list.append(admin["admin_username"].lower())
    return admin_list
def admins_password_list() :
    admins_password_list = []
    for admin in admins :
        admins_password_list.append(admin["password"]).lower()


def show_admins():
    print("current admins :")
    for admin in admins:
        print(f"{admin['admin_username']} - (${admin['name']})")


def save_admins():
    with open(admins_file, "w") as file:
        json.dump(admins, file, indent=4)


def find_admins_password(admin_username) :
    for admin in admins:
        if admin["admin_username"] == admin_username :
            return admin["password"]


def login_admins():
    username_counter = 0
    username_found = False
    print('Log In')
    while username_counter < 5 :
        input_username = input('\nenter your username :')
        if input_username in admins_list():
            print('username has found')
            username_found = True
            break
        elif input_username not in admins_list():
            print('admin username has not found . please try again .')
            while True :
                try:
                    input_for_try_again = input('do you want try again (yes/no) ? - ')
                    if input_for_try_again == 'no':
                        print('exit program ...')
                        exit(0)
                        break
                    elif input_for_try_again == 'yes':
                        break
                    else :
                        raise ValueError('Error.you must enter yes or no !')
                except ValueError as e :
                    print(e)
            username_counter += 1
            
        if username_counter >= 5:
                    print("You have reached the maximum attempts. Please contact another admin.")
                    print('exit program ...')
                    break
        
    if username_found == True:
        #password_correct = False
        password_counter = 0
        while password_counter < 5 :
            password = input("Enter your password: ")
            if password.startswith(' '):
                print("Invalid password. Please ensure it does not start with a space.")
                
            elif username_counter >= 5:
                    print("You have reached the maximum attempts. Please contact another admin.")
                    print('exit program ...')
                    break
            elif password != find_admins_password(input_username):
                print("password is  incorrect.")
                while True :
                    try:
                        input_for_try_again = input('do you want try again (yes/no) ? - ')
                        if input_for_try_again == 'no':
                            print('exit program ...')
                            exit(0)    
                        elif input_for_try_again == 'yes' :
                            break
                        elif input_for_try_again not in ['yes','no']:
                            raise ValueError('Error.you must enter yes or no !')
                    except ValueError as e :
                        print(e)
            else:
                #password_correct = True
                return "password is correct."
            password_counter += 1
    #if password_correct == False :
        #return




def fill_stocks():
    global board_games
    print('Fill stocks')
    print('\nGames List\n')
    show_board_games()
    print(50 * '*')
    
    while True:
        try:
            # Get input and normalize to lowercase
            input_board_game = input('Enter the name of the board game whose stock you want to fill: ').strip()
            normalized_game_list = [game.lower() for game in board_games_list()]  # Normalize game names
            
            # Check if the input game exists in the board games list
            if input_board_game.lower() in normalized_game_list:
                # Find the game object by matching case-insensitively
                for game in board_games:
                    if game["name"].lower() == input_board_game.lower():
                        print(f'{game["name"]} : current stock count - {game["stock"]}')
                        
                        # Get the filling stock amount
                        while True:
                            try:
                                input_filling_stock_amount = int(input('Enter filling amount: '))
                                if input_filling_stock_amount < 0:
                                    raise ValueError("Filling amount cannot be negative. Please enter again.")
                                break
                            except ValueError as e:
                                print(e)
                        
                        # Update the stock
                        game["stock"] += input_filling_stock_amount
                        print(f'{game["name"]} stock updated successfully.')
                        show_board_games()
                        save_updated_stock()
                        break
            
            else:
                raise ValueError('Entered board game is not in the list. Please enter again.')
        
        except ValueError as e:
            print(e)
            continue
        
        # Ask if the user wants to update another game's stock
        while True:
            try:
                input_another_filling_choice = input('Do you want to fill another game\'s stocks? (yes/no): ').strip().lower()
                if input_another_filling_choice == 'no':
                    break  
                if input_another_filling_choice.lower() not in ['yes','no']:
                    raise ValueError('error, you must enter yes or no !')
            except ValueError as e:
                print(e)
        if input_another_filling_choice == 'no':
            print('opperation is done')
            break
        

def add_admins():
    print("Please register by filling in your details.")
    while True:
        admin_username = input("Enter a admins username (at least 4 characters, no spaces): ")
        if len(admin_username) < 4 or ' ' in admin_username:
            print("Invalid username. Please ensure it is at least 4 characters long and contains no spaces.")
        elif any(a["admin_username"] == admin_username for a in admins):
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
        if any(c["email"] == email for c in admins):
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

    new_admin = {
        "admin_username": admin_username,
        "password": password,
        "name": name,
        "email": email,
        "city": city,
        "age": age,
        "gender": gender
    }
    admins.append(new_admin)
    save_admins()
    print(f"admin added successfully!")
    return new_admin


def remove_admins():
    show_admins()
    while True:
        try:
            input_admin_username_for_remove = input("Enter the admin's username you want to remove: ").strip().lower()
            
            # Assuming admins_list() returns a list of all admin usernames
            admins_usernames = [admin["admin_username"].lower() for admin in admins]
            
            if input_admin_username_for_remove in admins_usernames:
                print("Entered admin username is correct!")
                
                # Remove the admin
                admins[:] = [admin for admin in admins if admin["admin_username"].lower() != input_admin_username_for_remove]
                save_admins()
                
                print("Admin deleted successfully!")
                break
            else:
                raise ValueError("Entered admin username is not correct. Please try again!")
        except ValueError as e:
            print(e)


def admin_panel():
    if  login_admins():
        print("Welcome to the Admin Panel!")
        while True:
            print("1. Fill stocks")
            print("2. Add or remove admin")
            print("3. View all data")
            print("4. log out")

            while True:
                try:
                    # Prompt user for the main menu option
                    entered_num_for_prompt = int(input("\nEnter a number (1, 2,3 or 4): "))
                    if entered_num_for_prompt == 1:
                        fill_stocks()  # Assuming fill_stocks() is defined elsewhere
                        break
                    elif entered_num_for_prompt == 2:
                        print("\nAdmin Management:")
                        print("1. Add admin")
                        print("2. Remove admin")

                        # Inner loop for admin management
                        while True:
                            try:
                                input_num_admins_change = int(input("\nEnter 1 to add admin or 2 to remove admin: "))
                                if input_num_admins_change == 1:
                                    add_admins() # Assuming add_admins() is defined elsewhere

                                    break  # Exit the admin management loop
                                elif input_num_admins_change == 2:
                                    remove_admins()  # Assuming remove_admins() is defined elsewhere

                                    break  # Exit the admin management loop
                                else:
                                    raise ValueError("Invalid input! Please enter 1 or 2.")
                            except ValueError as er:
                                print(er)
                        break
                    elif entered_num_for_prompt == 3:
                        main_analytics_function()
                        print("Data displayed successfully!\n")

                        break
                    elif entered_num_for_prompt == 4:
                        break
                    else:
                        raise ValueError("Invalid input! Please enter 1, 2,3 or 4.")
                except ValueError as e:
                    print(e)
            if entered_num_for_prompt == 4:
                print('Log out...')
                break
            
            
if __name__ == "__main__":
    admin_panel()
