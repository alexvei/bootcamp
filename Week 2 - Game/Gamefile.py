import os       # built-in python module for operating system commands
import random   # built-in python module for generating randoms
import sys      # built-in python module for more system stuff
import time     # built-in python module for time


# Global Variables
father = 'glaen'
life = 3
name = ''
nor = 'nor'


# Functions
def cls():
    os.system('cls' if os.name=='nt' else 'clear')


def contin():
    input("Press enter to continue...")
    cls()

def life_system(lif):
    pass    


def entry_room():
    cls()
    choices = ["A", "B", "C"]

    message = """The Tomb of Akarak, A place laced within mystery and myth. 
    Some say the place holds the eternal hatred Akarak had for the living, as he practiced his necromancy within a secure chamber of the tomb. 
    Some say that this was his personal quarters, set up so he could hide away from the world. 
    Yet all knew the evil energies that lingered within this place, and treasures that had been stored away. 
    Countless magical items and gold beyond your belief await deep within his treasury. 
    As you approach, you notice this rather large living statue tower before you. 
    It's voice booms' "I am one of Akarak's few living guardians. Made of stone and souls that I am, an Araki your people know me as. 
    Yet to you, I pose a question. Akarak is... curious to see another so soon... 
    I see your pain adventurer, you venture into this tomb to save another, 
    yet you rush recklessly into danger without knowing the full truth. 
    Tell me then, What do you seek?"\n"""

    slow_writting(message)

    while True:
        player_choice = input('Answers: A:"Cure" B: "Power" C: "Riches."\n')
        if player_choice.upper() in choices:
            if player_choice.upper() == 'A':
                success_message = """A noble task indeed, Your heart and mind are perhaps strong enough to face my master's resting place. 
                Take this vessel to serve as a way to return from the plain of death and venture on, valiant soul.\n"""
                slow_writting(success_message)
                return 0
            else:
                print("Your heart is not pure, you will not survive. Leave this place and suffer the curse of Akarak!")
                input("Press enter to continue.")
                return 1   
            #After this, take away a life from the counter, ensure that we           
        else:
            print("Type only A, B or C.")
    
    

def dung_room_1():
    cls()
    message = """ As you enter the tomb. You are faced with a crypt, Coffins lie the walls and floors of this place, 
    nearly with names smudged out from sight and recognition, you can see some of the coffins located around. 
    After examination, you can see a few key names. They are wilfred daWldaddle, Ariana bleedhollow, riKi cruilla and yawn fEster. 
    Another Araki approaches you. It is much smaller and quieter than the last. It sits around your shoulders in height. 
    It speaks. "Here lies those devoted to Akarak's cause. Cultists, servants, preachers or warriors. 
    They all rest with their master no matter what. Most of these names have been lost to time. 
    Most of these bodies have withered and faded. Yet some live on, through us. 
    As their souls pilot these stone beings to greater success, and still tend to this tomb today.
    With this information, I ask this of you so you may advance further.

    Riddle:
    I am always near, but never far.
    I am always around, but never seen.
    I am often avoided, but I always catch up.
    I will come when your old and grey, or maybe even the very next day.
    I will come with cold embrace, and give you rest with a chill kiss on your face.
    I come in may forms whether it's irony, love, laughter, or hate.
    I am everyone's finale fate."""

    slow_writting(message)



def dung_room_3():
    pass


def lost():
    if life == 0:
        print("You died.")


def slow_writting(word):
    for c in word:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)
        


def welcome_message():
    global name
    slow_writting("Hello! A text-based adventure game.")
    time.sleep(0.2)
    name = input("\nEnter your name and let's get started: ")
    cls()
    

def story_intro():
    message = f"""Within the ruins of Akarak, lies an ancient and forgotten curse...
    Foolishly, your father {father.capitalize()} sought out these riches within the Tomb of Akarak, a place
    feared and known for being a perilous journey of twisting corridors
    and mind-boggling riddles. {father.capitalize()} failed to escape with the treasure, having to
    leave it behind to save their own life, Akarak's lingering will curse them
    to a fate worth that death. Immortally, but endless pain. They have been
    bedridden ever since and have lost themselves in their own torment.\n"""

    message_two = f""" You are {name.capitalize()}, You are the child of {father.capitalize()}. 
    He is suffering from the curse of Akarak, writhing in pain and anguish as it slowly eats away at them, 
    consuming their flesh and soul into nothing more than a mindless husk. 
    You began to search for answers, solutions, anything to help your father out to not see home rite and wither away into a shambling mound of madness. 
    A traveling old hermit visited your village of Ransburg, hailing themselves as an ex-disciple of Akarak.
    She was named {nor.capitalize()}, you asked for her aid, mention the situation with your father. 
    {nor.capitalize()} pondered this, examining {father.capitalize()} before telling you the way to save {father.capitalize()} is by delving into the tomb yourself 
    and claiming the riches of Akarak  and defeating their guardians of Knowledge. 
    His tests of knowledge were to be respected, not cheated. Lest you suffer the same fate as your father. 
    Resolute and determined, you ready your gear and venture into the tomb, knowing the dangers but knowing the benefits.\n"""

    slow_writting(message)

    contin()
    slow_writting(message_two)


cls()
welcome_message()
while True:
    cls()
    story_intro()

    while True:
        chc = input("Do you still want to continue? (y/n)")
        if chc.lower() == 'y':
            print(f"Great. Remember, you only have {life} lives. Be careful.")
            time.sleep(0.5)
            break

        if chc.lower() == 'n':
            print("Bye...")
            exit()
        else:
            print("Type y for yes, n for no.")

    if entry_room():
        pass
    else:
        dung_room_1()
        

