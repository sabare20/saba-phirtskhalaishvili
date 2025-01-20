
from customer_service import customer_panel
from admin_funqtions import admin_panel


def main():
    print('Enter 1 if you are customern.')
    print('Enter 2 if you are admin .')
    while True:
        input_customer_or_admin = int(input('Enter 1 or 2 :'))
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
            
        