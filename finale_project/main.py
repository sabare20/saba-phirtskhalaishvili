
"""
from customer_service import customer_panel
from admin_panel.admin_funqtions import admin_panel
customers_file = "finale_project/data/customers_data.json"
admins_file = "finale_project/data/admins_data.json"
"""
def main():
    print('enter 1 if you want to log in with admins account ')
    print('enter 2 if you are customer ')
    while True:
        input_customer_or_admin = int(input('enter 1 or 2 :'))
        if input_customer_or_admin == 1 :
            print('customer_panel()')
            break
        elif input_customer_or_admin == 2 :
            print('admin_panel()')
            break
        elif  input_customer_or_admin != 1 or input_customer_or_admin != 2 :
            print(' you must enter 1 or 2 !')
            
    
if __name__ == "__main__" :
    main()
            
        