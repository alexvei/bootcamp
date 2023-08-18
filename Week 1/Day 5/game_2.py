# Write a rock, paper, scissors game – for one player against the computer (the computer chooses at random
# Adapt the game so the user can enter the number of rounds they want to play
# Adapt the game to make it a two player game
import random


choices = ['ROCK', 'PAPER', 'SCISSORS']
# rock beats scissors
# 1 > 2

# paper beats rock
# 1 > 0

# scissor beats paper
# 2 > 1


def game_start():
    print("Welcome to a game of rock, paper and scissors!")
    while True:
        try:
            choose = input("(R)ock, (P)aper or (S)cissors? ")
            
            if choose.lower() == 'r':
                print("You've chosen ROCK.")
                return choices[0]
            if choose.lower() == 'p':
                print("You've chosen PAPER.")
                return choices[1]
            if choose.lower() == 's':
                print("You've chosen SCISSORS.")
                return choices[2]
        except ValueError:
            print("Enter r/p/s as a choice.")


def computer():
    global choices 
    comp_choice = random.choice(choices)
    print(f"The computer chose: {comp_choice}.")
    return comp_choice


def win(pl, np):
    if pl == np:
        print("Draw")
    if pl > np and np == 2:
        print("Player wins!")
    else:
        print("Computer wins!")

player = game_start()
npc = computer()
win(player, npc)