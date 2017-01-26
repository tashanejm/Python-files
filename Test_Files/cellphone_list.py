import cellphone


def main():

    phones = make_list()

    print("Here is the data you entered:")
    display_list(phones)


def make_list():
    phone_list = []

    print("Enter data for five phones.")
    for n in range(1,6):
        print("Phone number", str(n), ": ")
        man = input("Enter manufacture: ")
        mod = input("Enter model: ")
        price = float(input("Enter price: "))

        phone = cellphone.Cellphone(man,mod,price)
        phone_list.append(phone)
        
    return phone_list

def display_list(phones):
    for n in phones:
        print(n.get_manufact())
        print(n.get_model())
        print(format(n.get_price(), ",.2f"))
        print()
    
main()
