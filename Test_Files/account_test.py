import bankaccount2


def main():
    start_balance = float(input("Enter the about you'll like to start with "))

    account1 = bankaccount2.BankAccount(start_balance)

    pay = float(input("How much did you get paid this week? "))
    print("This amount will be deposit into your account",pay)
    account1.deposit(pay)
    
    print("Your balance is", account1.get_bal())

    amount = float(input("How much would you like to withdraw? "))
    account1.withdraw(amount)

    #print("Your balance is $", \
    #      format(account1.get_balance(), ",.2f"),sep="")
    print(account1)
main()
