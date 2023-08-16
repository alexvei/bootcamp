# we need the pin number and the amount to withdraw

def machine():
    money = int(input("Enter your balance: "))
    print(f'Your balance is: £{money}.')
    while (True):
        reply = input("Would you like to withdraw some money?(y/n) ")
        if (reply.lower() == 'y'):
            withdraw(money)
            break;
        elif (reply.lower() == 'n'):
            print("Okay, bye!")
            break;
        else:
            print("Please type only 'y' for yes or 'n' for no.")


def withdraw(amount):
    while (True):
        withdr = int(input("How much would you like to withdraw? "))
        if (withdr > amount or withdr < 0):
            print("Not enough money in the balance! Enter an appropriate amount or type 0 to exit.")
        elif (withdr == 0):
            print("Okay bye!")
            break;


while (True):
    response = input('Welcome. Would you like to check your balance?(y/n) ')
    if (response.lower() == 'y'):
        pin = input("Enter your pin number (must be 4 digits): ")
        machine()
        break;
    elif (response.lower() == 'n'):
        print("Okay, bye!")
        break;
    else:
        print("Please type only 'y' for yes or 'n' for no.")
    