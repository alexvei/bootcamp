import random

cards = ["Diamond", "Space", "Club", "Heart"]

desired_card = "Diamond"
current_card = " "

while current_card != desired_card:
    current_card = cards[random.randint(0,3)]
    print(f'{current_card}.')
print(desired_card, "has been found!")
