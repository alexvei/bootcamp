while True:
    try:
        number= int(input("Give a number to split in 2: "))
        break
    except ValueError:
        print("Enter an integer please.")

if number % 2:
    halves = (number - 1) / 2
    half_a = int(halves)
    half_b = int(halves) + 1
    
    print(f"The number is split into {half_a} and {half_b}.")

else:
    halves = int(number / 2)
    print(f"The number is split into {halves} and {halves}. ")
