def multiplication_table(num):
    for i in range(1,13):
        print(num*i)

def question(a):
    a = input("Would you like to get the table for a different number?(y/n) ")
    if a.lower() == 'y':
        return True
    if a.lower() == 'n':
        print("Ok, bye!")
        return False
    else:
        print("Please only y/n answers.")
        question(a)


while True:
    while True:
        try:
            number = int(input("Enter a number: "))
            break
        except ValueError:
            print("Not a number.")

    multiplication_table(number)
    a = ''
    if question(a):
        pass
    else:
        break