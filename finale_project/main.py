
from customer_service import customer_panel
from admin_funqtions import admin_panel


def main():
    print('enter 1 if you want to log in with admins account ')
    print('enter 2 if you are customer ')
    while True:
        input_customer_or_admin = int(input('enter 1 or 2 :'))
        if input_customer_or_admin == 1 :
            customer_panel()
            break
        elif input_customer_or_admin == 2 :
            admin_panel()
            break
        elif  input_customer_or_admin != 1 or input_customer_or_admin != 2 :
            print(' you must enter 1 or 2 !')
            
    
if __name__ == "__main__" :
    main()
            
        