# # IM BORED SO LETS MAKE A GUESSING GAME.
# import random

# x = random.randint(1,100)
# tries = 0
# guess = 0
# while(True):
#     tries += 1
#     guess = int(input("Guess the number: "))
#     if (guess > x):
#         print("Try a smaller number")
#     if (guess < x):
#         print("Try a bigger number")
#     if (guess == x):
#         break
    
# print(f"Nice, you guessed it after {tries}. The number was indeed {x}.")

age = int(input("What's your age? "))
country = input("Which country are you from? ")
if (age >= 18 and country == "UK"):
    print("Yes, I can serve you.")
else:
    print("You aren't old enough.")
