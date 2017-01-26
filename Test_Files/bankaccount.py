class BankAccount:
    def __init__(self,bal):
        self.__balance = bal
    def deposit(self,amount):
        self.__balance += amount
        #return self.__balance
    def withdraw(self, amount):
        if amount <= self.__balance: self.__balance-= amount
        else: print("Error: Insufficient funds")
    def get_balance(self):
        return self.__balance
    def __str__(self):
        return 'The balance is $'+ format(self.__balance, ',.2f')
