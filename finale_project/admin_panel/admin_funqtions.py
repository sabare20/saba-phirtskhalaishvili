import json
import os
from finale_project.customer_service import show_board_games

board_game_file = "finale_project/data/board_games_data.json"
sales_file = "finale_project/data/sales_data.json"
customers_file = "finale_project/data/customers_data.json"


if os.path.exists(board_game_file):
    with open(board_game_file, "r") as file:
        board_games = json.load(file)
else:
    board_games = []

if os.path.exists(sales_file):
    with open(sales_file, "r") as file:
        sales = json.load(file)
else:
    sales = []

if os.path.exists(customers_file):
    with open(customers_file, "r") as file:
        customers = json.load(file)
else:
    customers = []


def board_games_list():
    board_game_list = []
    for game in board_games :
        board_game_list.append(game['name'])
    

def fill_stocks():
    print('Fill stocks')
    print('\nGames List')
    show_board_games()
    while True :
        input_board_game = input('enter name of board game whichs stock you want to fill')
        if input_board_game not in board_games_list:
            print()
    

def remove_board_game():
    print('enter games name which you want to remove :')


def add_admins():
    print('enter admins name which you want to add .')


def remove_admins():
    print('enter admins name which  u want to remove .')
    

def admin_panel():
    print('welcome')
    print('base data :')
    print('\nenter 1 if you want to fill stocks ')
    print('enter 2 if you want to remove boardgame ')
    print('enter 3 if you want to add or remove admin')
    #print('enter 4 if you want to see whole data .')
    
    while True:
        try:
            entered_num_for_prompt = int(input('\nenter number 1 , 2 or 3 :'))
            if entered_num_for_prompt == 1:
                fill_stocks()
            elif entered_num_for_prompt == 2:
                remove_board_game()
            elif entered_num_for_prompt == 3:
                print('\nenter 1 if you want to add admin ')
                print('enter 2 if you want to remove admin ')
                while True:
                    try:
                        input_num_admins_change = int(input('\nenter number 1 or 2 :'))
                        if input_num_admins_change == 1 :
                            add_admins()
                        elif input_num_admins_change == 2 :
                            remove_admins()
                        elif input_num_admins_change not in [1,2]:
                            raise ValueError("you must enter number 1 or 2 !")
                        break
                    except ValueError as er:
                        print(er)
            elif entered_num_for_prompt not in [1,2,3]:
                raise ValueError("you must enter 1,2 or 3 !")
            break
        except ValueError as e:
            print(e)


    