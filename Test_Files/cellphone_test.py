import cellphone

def main():
    try:
        man = input("Enter manufacture: ")
        mod = input("Enter model: ")
        price = input("Enter price: ")

        phone = cellphone.Cellphone(man,mod,price)

        print("Here is the data you have entered")
        print("Manufacture: " + phone.get_manufact())
        print("Model: " + phone.get_model())
        print("Price: $" + format(phone.get_price(), ",.2f"))

    except IOError as num:
        print(num)
main()
