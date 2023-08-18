import random


def roll(num):
    total_dices = []
    for i in range(0, num):
        total_dices.append(random.randint(1, 6))
    
    return total_dices


def total_score(dice_list):
    sum = 0
    for i in dice_list:
        sum += i
    return sum


def player(val):
    while True:
        try:
            
                throws = int(input("How many times do you want to throw the dice, player {}? ".format(val)))
                if 0 <= throws <= 5:
                    break
                else:
                    print("That's a bit unreasonable now isn't it...")
        except ValueError:
            print("Not an integer.")
    
    return roll(throws)


def game_start():
    global total_players
    while True:
        try:
            total_players = int(input("How many people are playing this game? "))
            if 1 <= total_players <= 4:
                break
            elif total_players == 0:
                print("Ok, bye!")
                exit()
            else:
                print("A reasonable number...")
        except ValueError:
            print("Not an integer.")

game_start()
player_list = []
for i in range(total_players):
    player_list.append(player(i+1))

for i in range(total_players):
    print(f"Player {i+1} has rolled: {player_list[i]}, which amounts to a total of {total_score(player_list[i])}.")
