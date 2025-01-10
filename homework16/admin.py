import random

from homework16.common import process_user_input
from homework16.db import sessions
def admin_sign_in():
    admin_data={'admin_ID':'admin_pasword'}
    input_admin_ID=input('enter your admin_ID :')
    input_admin_pasword=input('enter pasword :')
    if input_admin_ID in admin_data.keys and input_admin_pasword==admin_data[input_admin_ID]:
        print('signed in successfully !')
    else:
        print('invalid ID or pasword.please try again')
        return admin_sign_in()
def list_admin_menu_items():
    print("1. list all sessions ")
    print("2. remove session")
    print("3. add session")
    print("4. edit session")
    return process_user_input()
def greetings():
    print("Welcome to the admin panel")
    print("Please sign in to continue")
def add_session():
    print("Adding session")
    print("Enter the session details")
    film_name = input("Film name: ")
    start_time = input("Start time: ")
    room_number = input("Room number: ")
    room_length = int(input("Room length: "))
    room_width = int(input("Room width: "))
    capacity = room_length * room_width
    # TODO: session_id may be used already, need to check
    session_id = random.randint(1, 1000)
    session = {
        "session_id": session_id,
        "film_name": film_name,
        "start_time": start_time,
        "room_number": room_number,
        "room_length": room_length,
        "room_width": room_width,
        "capacity": capacity
    }
    print("Session added successfully")
    sessions.append(session)
def list_sessions():
    print("Listing sessions")
    if not sessions:
        print("No sessions found")
        return
    for session in sessions:
        print(f"\tSession ID: {session['session_id']}")
        print(f"\tFilm name: {session['film_name']}")
        print(f"\tStart time: {session['start_time']}")
        print(f"\tRoom number: {session['room_number']}")
        print(f"\tRoom length: {session['room_length']}")
        print(f"\tRoom width: {session['room_width']}")
        print(f"\tCapacity: {session['capacity']}")
        print("\n")       
def remove_sessions():
    if not sessions:
        print("No sessions found")
        return
    session_in_sessions=False
    input_remove_session_id=input('enter session_id which you want to remove :')
    for session in sessions:
        if session['session_id']==input_remove_session_id:
            sessions.remove(session)
            session_in_sessions=True
    if session_in_sessions==False:
        print('session with entered id is not found.please enter correct Session ID')
       
def edit_session():
    if not sessions:
        print("No sessions found")
        return
    session_in_sessions=False
    input_edit_id=input('enter session_id which you want to edit :')
    input_edit_key=input('enter which parameter want to edit :')
    for session in sessions:
        if session['session_id']==input_edit_id:
            input_updated_value=input('enter new value :')
            session[input_edit_key]=input_updated_value
            print(f'\tnew {input_edit_key} is - {input_updated_value} ')
            print('session edited successfully')
            session_in_sessions=True
    if session_in_sessions==False:
        print('session with entered id is not found.please enter correct Session ID')
    
def admin_loop():
    greetings()
    admin_sign_in()
    while True:
        user_input = list_admin_menu_items()
        match user_input:
            case "1":
                list_sessions()
            case "2":
                print("Removing session")
                remove_sessions()
            case "3":
                add_session()
            case "4":
                print("Editing session")
                edit_session()
            case _:
                print("Invalid input")
print(admin_loop())