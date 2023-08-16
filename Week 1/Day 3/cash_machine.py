
money = -1

def machine():
    global money
    while (money < 0):
        try:
            money = int(input("Enter your balance: "))
        except ValueError:
            print("That's not a number!")
    
    print(f'Your balance is: £{money}.')
    if (money == 0):
        print("You have no money left in your bank account.")
        return 
    while (True):
        reply = input("Would you like to withdraw some money?(y/n) ")
        if (reply.lower() == 'y'):
            while True:
                withdraw(money)
                if money == 0:
                    print("No more money left in the bank!")
                    return
                cont = input("Do you want to withdraw more money?(y/n) ")
                if cont == 'y':
                    pass;
                elif cont == 'n':
                    break;
                else:
                    print("Enter 'y' for yes or 'n' for no please.")

        elif (reply.lower() == 'n'):
            print("Okay, bye!")
            break;
        else:
            print("Please type only 'y' for yes or 'n' for no.")


def withdraw(amount):
    global money
    while (True):
        while (True):
            try: 
                withdr = int(input("How much would you like to withdraw? "))
                break;
            except ValueError:
                print("That's not a number!")
        
        if (withdr > amount):
            print("Not enough money in the balance! Enter an appropriate amount or type 0 to exit.")
        elif (withdr < 0):
            print("Invalid input.")
        elif (withdr == 0):
            print("Okay bye!")
            break;
        else:
            print(f'Money withdrawn: £{withdr}.')
            print(f'New balance: £{amount-withdr}.')
            money = amount-withdr
            break;


while (True):
    response = input('Welcome. Would you like to check your balance?(y/n) ')
    if (response.lower() == 'y'):
        pin = 0
        while (pin < 1000 or pin > 9999):
            try:
                pin = int(input("Enter your pin number (must be 4 digits): "))
            except ValueError:
                print("That's not a number!")
        machine()
        break;
    elif (response.lower() == 'n'):
        print("Okay, bye!")
        break;
    else:
        print("Please type only 'y' for yes or 'n' for no.")
    