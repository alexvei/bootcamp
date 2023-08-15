num = int(input("Enter a number: "))

if (num%3 == 0) and (num%7 == 0):
    print("fizz buzz")
elif (num%3 == 0):
    print("fizz")
elif (num%7 == 0):
    print("buzz")
else:
    print(num)
