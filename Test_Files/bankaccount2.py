class BankAccount:

    def __init__(self, bal):
        self.__bal = bal

    def deposit(self, amount):
        self.__bal += amount

    def withdraw(self, amount):
        if amount > self.__bal:
            print("Error,  Insufficient funds")
        else:
            self.__bal -= amount

    def get_bal (self):
        return self.__bal

    
    def __str__(self):
        return "The balance is $" + format(self.__bal, ",.2f")
