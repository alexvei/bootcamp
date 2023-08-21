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
    

def dung_explore_1():
    while True:
        choice = input("Explore y/n: ")
        if choice == 'y':
            explore_message = ("\tAs you pay respect to those who have fallen before you, they return the generosity in kind.\n"
            "\tAllowing another notch with your vessel to fill, granting you a burst of vigor.\n"
            "\tYou venture deeper, knowing that those of the past are cheering you on from the afterlife.\n\n")
            slow_writting(explore_message)
            print("\tYou've gained 1 life!", f"Total: {life}.")
            contin()
            life_system(1)
            return 1
        elif choice == 'n':
            return 1
        else:
            print("y/n only.")


def dung_explore_2(): # Placeholder
    pass


def dung_room_1():
    cls()
    message = ("As you enter the tomb...\n"
    "You are faced with a crypt, Coffins lie the walls and floors of this place, \n"
    "nearly with names smudged out from sight and recognition, you can see some of the coffins located around. \n"
    "After examination, you can see a few key names. They are wilfred daWldaddle, Ariana bleedhollow, riKi cruilla and yawn fEster.\n" 
    "Another Araki approaches you. It is much smaller and quieter than the last. It sits around your shoulders in height.\n" 
    "It speaks. \"Here lies those devoted to Akarak's cause. Cultists, servants, preachers or warriors.\n" 
    "They all rest with their master no matter what. Most of these names have been lost to time.\n" 
    "Most of these bodies have withered and faded. Yet some live on, through us.\n" 
    "As their souls pilot these stone beings to greater success, and still tend to this tomb today.\n"
    "With this information, I ask this of you so you may advance further.\n\n"
    "Riddle:\n"
    "\tI am always near, but never far.\n"
    "\tI am always around, but never seen.\n"
    "\tI am often avoided, but I always catch up.\n"
    "\tI will come when your old and grey, or maybe even the very next day.\n"
    "\tI will come with cold embrace, and give you rest with a chill kiss on your face.\n"
    "\tI come in many forms whether it's irony, love, laughter, or hate.\n"
    "\tI am everyone's finale fate.\n")

    slow_writting(message)
    
    while True:
        print(f"Lives left= {life}")
        player_answer = input('Answer: ')

        if player_answer.lower() == 'death':
                success_message = ("\tYour memory is sharp, I implore you to venture on.\n"
                "\tBut you may pay respects to those who have fallen before you, they rest within these halls.\n"
                "\tPerhaps they will give you the strength and courage to venture deeper into our master abode.\n")
                slow_writting(success_message)
                contin()
                return dung_explore_1()
        else:
            life_system(0)
            if life == 0:
                print(""" "You do not know? Perhaps I shall show you!"
                      As it shouts, the coffins burst open and fleshless beings erupt from them. 
                      You are surrounded, with no hope to escape as the door shuts behind you.
                      "You will share the fate of these people... as many others have before"
                      As the skeletons shove you into a new coffin. And etch your name onto the front.""")
                contin()
                return False


def dung_room_2(): # Placeholder
    pass


def entry_room():
    choices = ["A", "B", "C"]
    global life

    message = (f"\tThe Tomb of Akarak, A place laced within mystery and myth.\n" 
    "Some say the place holds the eternal hatred Akarak had for the living, as he practiced his necromancy within a secure chamber of the tomb.\n" 
    "Some say that this was his personal quarters, set up so he could hide away from the world.\n" 
    "Yet all knew the evil energies that lingered within this place, and treasures that had been stored away.\n" 
    "Countless magical items and gold beyond your belief await deep within his treasury.\n" 
    "As you approach, you notice this rather large living statue tower before you.\n" 
    "It's voice booms' \"I am one of Akarak's few living guardians. Made of stone and souls that I am, an Araki your people know me as.\n" 
    "Yet to you, I pose a question. Akarak is... curious to see another so soon...\n" 
    "I see your pain adventurer, you venture into this tomb to save another,\n"
    "yet you rush recklessly into danger without knowing the full truth.\n" 
    "Tell me then, What do you seek?\"\n")

    slow_writting(message)

    while True:
        player_choice = input('Answers: A:"Cure" B: "Power" C: "Riches"\t\t Lives left= {}\nAnswer: '.format(life))
        if player_choice.upper() in choices:
            if player_choice.upper() == 'A':
                success_message = ("\tA noble task indeed, Your heart and mind are perhaps strong enough to face my master's resting place.\n" 
                "\tTake this vessel to serve as a way to return from the plain of death and venture on, valiant soul.\n")
                slow_writting(success_message)
                contin()
                return True
            else:
                life_system(0)
                if life == 0:
                    print("Your heart is not pure, you will not survive. Leave this place and suffer the curse of Akarak!")
                    contin()
                    return False
                             
        else:
            print("Type only A, B or C.")


def globals():
    global father, life, name, nor
    father = 'Glaen'
    life = 3
    nor = 'nor'


def life_system(action): # Placeholder
    global life
    if action:
        life += 1
    else:
        life -= 1
        print("Wrong!")


def lost(): # Placeholder
    pass


def slow_writting(word):
    for c in word:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0) ## 0 for debugging
        

def story_intro():
    message = (f"Within the ruins of Akarak, lies an ancient and forgotten curse...\n"
    f"Foolishly, your father {father.capitalize()} sought out these riches within the Tomb of Akarak, a place\n"
    "feared and known for being a perilous journey of twisting corridors\n"
    f"and mind-boggling riddles. {father.capitalize()} failed to escape with the treasure, having to\n"
    "leave it behind to save their own life, Akarak's lingering will curse them\n"
    "to a fate worth that death. Immortally, but endless pain. They have been\n"
    "bedridden ever since and have lost themselves in their own torment.\n")

    message_two = (f"You are {name.capitalize()}, You are the child of {father.capitalize()}.\n" 
    "He is suffering from the curse of Akarak, writhing in pain and anguish as it slowly eats away at them, consuming their flesh and soul into nothing more than a mindless husk.\n" 
    "You began to search for answers, solutions, anything to help your father out to not see home rite and wither away into a shambling mound of madness.\n" 
    "A traveling old hermit visited your village of Ransburg, hailing themselves as an ex-disciple of Akarak.\n"
    f"She was named {nor.capitalize()}, you asked for her aid, mention the situation with your father.\n"
    f"{nor.capitalize()} pondered this, examining {father.capitalize()} before telling you the way to save {father.capitalize()} is by delving into the tomb yourself\n" 
    "and claiming the riches of Akarak  and defeating their guardians of Knowledge.\n" 
    "His tests of knowledge were to be respected, not cheated. Lest you suffer the same fate as your father.\n" 
    "Resolute and determined, you ready your gear and venture into the tomb, knowing the dangers but knowing the benefits.\n")

    slow_writting(message)
    contin()
    slow_writting(message_two)


def welcome_message():
    global name
    slow_writting("Hello! A text-based adventure game.")
    time.sleep(0.2)
    name = input("\nEnter your name and let's get started: ")
    cls()


cls()
welcome_message()
while True:
    cls()
    globals()
    story_intro()

    while True:
        chc = input("Do you still want to continue? (y/n)")
        if chc.lower() == 'y':
            input(f"Great. Remember, you only have {life} lives. Be careful. \nPress enter to continue...")
            break
        if chc.lower() == 'n':
            print("Bye...")
            exit()
        else:
            print("Type y for yes, n for no.")
    
    cls()
    pass_1 = entry_room()
    if pass_1:
        pass_2 = dung_room_1()
    if pass_2:
        pass_3 = dung_room_2()
        


    #Writing needs to be sped up, for the amount of wording we have, the text crawl needs to be turned into a text walk. Add more time for people to read until going to the next chapter.
    #Maybe using an input system for (Press enter to continue) or something of the like.
    #The Life check counter needs to be around for a little bit longer so people can actually make note of their life count.
    