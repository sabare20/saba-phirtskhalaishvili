class BankAccount:
    def __init__(self,balance):
        self._balance = balance
    
    def set_balance(self,v):
        self._balance = v
    
    def get_balance(self):
        return self._balance
    
    def deposit(self,amount):
        if type(amount) != int:
            print('Error! type of amount must be int .')
            return
        if amount <= 0 :
            raise ValueError('deposit amount must be positive !')
            
        self._balance += amount
    
    def withdraw(self,amount):
        if type(amount) != int:
            print('Error! type of amount must be int .')
            return
        if amount <= 0 :
            raise ValueError('withdraw amount must be positive !')
            
        elif self._balance - amount < 0:
            print('not enough balance')
            return
        else:
            self._balance -= amount
    
    def get_balance(self):
        return self._balance
    
    
def main():
    account = BankAccount(500)
    account.deposit(-200)
    print(account.get_balance())
    account.withdraw(8000)
    print(account.get_balance())

if __name__ == '__main__':
    main()
    
        
    
    