import os       # built-in python module for operating system commands
import random   # built-in python module for generating randoms
import sys      # built-in python module for more system stuff
import time     # built-in python module for time


# Global Variables #############################################################
father = 'glaen'
name = ''
nor = 'nor'
life = 3
################################################################################


# Functions ####################################################################
# Clear the screen
def cls():
    os.system('cls' if os.name=='nt' else 'clear')


# Press enter to continue
def contin():
    input("Press enter to continue...")
    cls()
    

################################################################################
# Dungeon explore options
def dung_explore_1(): # This is exploration after puzzle 2
    explore_message = ("As the far side tomb door raises up, you are left with a room with the Akari and the tombstones and coffins dotted about this place.\n"
    "You wonder what the usage for those were, who the people are inside the coffins and what they did for their master...\n"
    "The room is rather dark and murky, dirt and muck being on some of the coffins as dust covers the entire floor, most of the tombstones are smudged beyond belief apart from a few.\n"
    "The Akari goes back to cleaning and maintaining the tombstones, seemingly dysfunctional for a while till you came and opened the place up again.\n"
    'The Akari speaks. "Pay respects to the dead while you are here... perhaps it will gain you favor among our gods and Akarak.".\n\n')
    slow_writting(explore_message)

    print("You can:")
    print("\t1. Venture on.")
    print("\t\t2. Speak to the Akari.")
    print("\t\t\t3. Honor the dead.")
    print("\t\t\t\t4. Open a coffin.")

    while(True):
        try:
            b_choice = int(input("Choose one of the 4: "))
            if 1 <= b_choice <= 4:
                break
            else:
                print("A number from 1-4")
        except ValueError:
            print("A number please. (1-4)")
    if b_choice == 1:
        message = ("You ignore the request of the Akari, venturing down into the darker depths.\n"
                   "The Akari looks at the door you head towards. Sighing.\n"
                   '"Perhaps another one will remember you all..."\n'
                   "As it goes back to maintain the grim serenity within the walls...\n")
        
        slow_writting(message)
        contin()
        return 1
    
    if b_choice == 2:
        message = ("You walk up to the Akari, seemingly feeling saddened or empty as it continues its duties with the littlest effort possible.\n"
                   "It looks up to you, speaking in a gravelly and monotone voice.\n"
                   '"What do you wish mortal… our home is not for one with so much life within." You ask about it.\n'
                   "It pauses for a moment, entertaining the thought. Before looking up to you.\n"
                   '"You wish to learn about the grave digger? I find that amusing… but I will humor you. My name before my vessel was Utia, I wandered these halls in silence, I dared not speak."\n'
                   'You ask why. "The dead can hear you, I wish to honor their conversations so I do not interrupt..."\n' 
                   'You blink, clearly shocked at how casually it said this. "I assure you, they mean no harm... only are curious, like most humans before…"\n'
                   'It looks down, returning to its duties. “Walk away mortal. Before they claim you as well.\n"'
                   "You nod quickly, before hurrying down the staircase. Not before noting the smile on Utia's face.\n\n")
        
        slow_writting(message)
        contin()
        return 1
    
    if b_choice == 3:
        message = ("You look towards one of the coffins, saying a prayer for them to wish them a blissful rest.\n"
                   "The Akari sees this, shocked and happy. It walks up to you, extending its marble palm as you see an Orb of life.\n"
                    "\"It is rare to see one so respectful of the past... you deserve to be rewarded. I hope this proves a lesson to you just as much as it did for me.\"\n"
                    "You take the orb of life and place it into your vessel, it thrums with energies as you embrace it.\n"
                    "The dead stand with you, as allies. Willing to retrieve you from whatever afterlife you find yourself in.\n"
                    "You head towards the doorway, nodding in thanks towards the Akari before heading down. It waves as you do.\n\n")
        
        slow_writting(message)
        contin()
        return 1
    if b_choice == 4:
        message = ("Your curiosity gets the better of you, as you see a coffin slightly open in the back that appears to have a glint of something.\n"
                   "As you walk towards it, the Akari warns you. \"Do you so wish to throw away your life so willingly? Perhaps it is best for you to turn back.\""
                    "You look at it disapprovingly, as you move the coffin. The denizen grabs you as it lurches out of the coffin.\n"
                    "Dragging you in and closing it behind you. The Akari merely sighs. As it looks to your now floating spirit.\n"
                    '"A shame... Perhaps it\'s best for your to remain here... till we can forge you a vessel for yourself..."\n\n')
        
        cls()
        slow_writting(message)
        contin()
        return 0


def dung_explore_2(): # This is exploration after puzzle 3
    explore_message = ("As the trial is complete in this room, you look around the entire room. Trying to glean what you can.\n"
    "The floor is in absolute chaos as books and tomes litter the floor, multiple pages ripped out lie next to them, all from differing volumes.\n"
    "The bookshelves seem precariously balanced off each other, if it were to move even just a tiny bit, they could collapse and cause serious damage to this entire room. \n"
    "After you move some of the books and pages, you see necromantic sigils that seem innate.\n"
    "What do you do?\n")
    slow_writting(explore_message)

    print("You can:")
    print("\t1. Look at the books on the table.")
    print("\t\t2. Venture deeper")
    print("\t\t\t3. Examine the sigils")

    while(True):
            try:
                b_choice = int(input("Choose one of the 3: "))
                if 1 <= b_choice <= 3:
                    break
                else:
                    print("A number from 1-3")
            except ValueError:
                print("A number please. (1-3)")

    if b_choice == 1:
            message = ("You look at the books on the table, your innate curiosity opens some of these books.\n"
                    "Most of these are merely just books on history of the past yet one seems special as it sits almost destroyed and caped in dust.\n"
                    "You blow against it, opening it up to see a Journal.\n"
                    "It reads:\n"
                    "\n"
                    "\"Day 224, I have finally found a way to focus my magic.\n"
                    "Too long has it been uncontrollable within the wrong hands, the mortals of the village nearby have been much too insistent on desecrating my place of rest.\n"
                    "My subject's place of rest. With this focus… My disciples will finally have a means to control this power of theirs… safely…\"\n"
                    "\n"
                    "The focus? You think, you wonder if this can help you with your father\'s curse.\n"
                    "As you place the book down, you turn to the door.\n"
                    "Continuing on into the depths of the tomb…\n")

            slow_writting(message)
            contin()
            return 1
        
    if b_choice == 2:
            message = ("You realize how much effort that may come from examining everything in this room, and it has overwhelmed you.\n"
                    "You decide a better use of your time is to venture on down into the depths.\n")
            
            slow_writting(message)
            contin()
            return 1
        
    if b_choice == 3:
            message = ("You lean down towards the sigils, wanting to get a closer look, you aren\'t sure of the language of the runes that are on there but you notice something as you move pages out of the way of the full circle, a dulled out life orb.\n"
                    "It seems weak but it has enough to keep you going in your adventure you think.\n"
                    "As you place it into your vessel, it thrums weekly, the vessel begins to slowly empower it, reaching a level where it\'s as bright as the other Orbs that you have seen on your adventure.\n"
                    "(Gain +1 Life!)\n"
                    f"Total: {life+1} lives.\n"
                    "With this, you head down to the depths, seeing what horors await you.\n")
            
            cls()
            slow_writting(message)
            contin()
            life_system(1)
            return 1


def dung_explore_3(): # This is exploration after puzzle 4
    pass


def dung_explore_4(): # This is exploration before puzzle 5
    global life
    explore_message = ("Finally, you arrive at the depths of Akarak's tomb.\n"
    "A wide open room with a large entry way on both the left and right of the room stands tall.\n"
    "You notice a large stone coffin in the middle of the room.\n" 
    "You steel yourself, approaching the coffin and reading it.\n"
    "\"Akarak, The abandoned lich\" it read.\n" 
    "Your eyes scan the room around you again, from the middle,\n"
    "you see a stone tablet on the opposite side of the entryway with empty holes.\n\n")
    slow_writting(explore_message)

    print("You can:")
    print("\t1. Look into the large archway on the right.")
    print("\t\t2. Approach the tablet.")
    print("\t\t\t3. Loot the place")

    while(True):
        try:
            b_choice = int(input("Choose one of the 3: "))
            if 1 <= b_choice <= 3:
                break
            else:
                print("A number from 1-3")
        except ValueError:
            print("A number please. (1-3)")
    if b_choice == 1:
        message = ("You look through the large archway, seemingly not seeing much beyond darkness.\n" 
                   "A small glint however shines through. As you walk towards it, you notice it’s a life orb.\n"
                   "You pick it up and add it to your vessel.\n"
                   "Handy. (Gain +1 Life)\n"
                   f"Total Lives: {life+1}\n\n")
        cls()
        life_system(1)
        slow_writting(message)
        contin()
        return True
    
    if b_choice == 2:
        return dung_room_4()
    
    if b_choice == 3:
        life -= 1
        message = ("You see some gold and jewels littering the sides of the room,\n"
                   "your greed overtakes you as you reach for a pile of gold.\n"
                   "As you touch it, your hand instantly falls off.\n" 
                   "You shriek before seeing a warning carved onto the wall behind the gold.\n"
                   "\"Touching this hoard will result in the demise of the appendage that touched it. Be careful Akari.\" it states.\n" 
                   "You sigh before pulling out a life vessel, aiming to heal off the damage before you bleed out.\n"
                   "(Lose 1 Life)\n"
                   f"Total lives: {life}\n\n")
        
        cls()
        slow_writting(message)
        

        if life == 0:
            print("You have no life vessel to help stop the bleeding, you feel your body fail as you fall to the ground. Undone by Greed.")
            contin()
            return False
        contin()
        return True
    

################################################################################
# Dungeon puzzles
def dung_room_1(): # Puzzle 2
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
                fail_message = ("You do not know? Perhaps I shall show you!\n"
                      "As it shouts, the coffins burst open and fleshless beings erupt from them.\n" 
                      "You are surrounded, with no hope to escape as the door shuts behind you.\n"
                      '\"You will share the fate of these people... as many others have before\"\n'
                      "As the skeletons shove you into a new coffin. And etch your name onto the front.\n\n")
                contin()
                return False


def dung_room_2(): # Puzzle 3
    cls()
    message = ("As you hop off the last step, you are left with what appears to be a rundown Ritual room.\n"
    "Books and tomes scatter the floor as bookcases seem to have toppled upon themselves.\n"
    "You can climb through some of the passageways created by the toppled bookshelves and reach a pedestal.\n"
    "There sits a book, with a bookmarked page.\n"
    "You open the book to the page and see it written in fine ink.\n"
    '"To those that read this and are not of my troupe, I ask this of you, around this room are the remnants of my study. Where I practiced my forbidden magics and held my darkest secrets,\n'
    'for whatever reason you chose to venture into this sacred place, I ask this of you. Who is the disciple I sent off to the realm of the living,\n'
    'to explore and learn more about life and death?"\n\n')

    slow_writting(message)
    while True:
        print(f"Lives left= {life}")
        player_answer = input('Answer: ')

        if player_answer.lower() == 'nor': 
            success_message = ("\tNor... yes... I do miss her... I trust she is finding your realm suitable...\n"
            "\tI implore you to venture deeper, you seem wiser than the rest...\n"
            "\tYet if you wish to learn more, read some of the books on this table...\n")

            slow_writting(success_message)
            contin()
            return dung_explore_2()
        
        else:
            life_system(0)
            if life == 0:
                fail_message = ("You have failed to answer the question correctly in three attempts.\n"
                            "The book closes on you, the doors closing and leaving you trapped.\n"
                            "The sigils of the room light up as necrotic energy primates through the air.\n"
                            "You feel yourself slowly wither, as you watch as the spirit of Akarak guides you to the next life.\n")
                
                slow_writting(fail_message)
                contin()
                return False   


def dung_room_3(): # Puzzle 4
    return True


def dung_room_4(): # Puzzle 5
    cls()
    message = ("As you approach the tablet, you see a riddle written on it.\n"
                "\"Throughout your journey down in my depths, you have learnt more of my presence in the world. My motives and my treatment of others. Now I ask this of you, outsider.\n"
                "Fill in the word below the tablet, and it shall allow you into my focus.\"\n"
                "Below you see every single letter of the alphabet placed down in a chest. Fitting perfectly towards the tablet. What will you spell?\n\n")
            
    slow_writting(message)
    
    while True:
        print(f"Lives left= {life}")
        player_answer = input('Answer: ')

        if player_answer.lower() == 'wake':
            success_message = ("The walls rumble as the wall behind the tablet raises. Showing a staff of malicious energies.\n" 
                                "Akarak's focus.\n" 
                                "You take it, and venture outwards, seemingly conquering the challenges.\n")
            slow_writting(success_message)
            contin()
            return True
        
        else:
            life_system(0)
            if life == 1:
                print("Wake up! This is your last chance!")
            elif life == 0:
                print("You hear a large opening of the coffin behind you, this shriveled corpse steps out and looks at you.\n" 
                        "It speaks slowly.\n"
                        "\"You… have… learnt… NOTHING!\"\n" 
                        "As the corpse lashes out, grabbing you with lightning speed and pulling you into its resting place.\n" 
                        "The top of the coffin sliding on top as you are trapped in Akarak's tomb.\n")
                contin()
                return False
            

################################################################################
# Entry room and entry room explore options ####################################
################################################################################
def entry_room(): # Puzzle 1
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
                return entry_room_explore()
            else:
                life_system(0)
                if life == 0:
                    print("Your heart is not pure, you will not survive. Leave this place and suffer the curse of Akarak!")
                    contin()
                    return False
        else:
            print("Type only A, B or C.")


def entry_room_explore(): # This is exploration for puzzle 1
    explore_message = ("\tThe Akari stands back and lets you gather your surroundings.\n"
    "You stand at the base of the tomb, it stands tall as it's in the base of a large mountain, the tomb's door is circular as it rolls sideways to allow you to enter the tomb.\n"
    "Two pillars stand broken at the entryway, the rubble spreading across the stone path.\n"
    "The Akari stands leaning against the wall.\n"
    "Its figure is so tall that you have to lean your neck upwards to see its head. It looks like a stone lion as it merely watches you, it doesn't appear like it wants to talk.\n\n")
    slow_writting(explore_message)
    print("You can:")
    print("\t1.Venture into the tomb,")
    print("\t\t2.Look at the Pillars")
    print("\t\t\t3.Try to talk to the Akari.")
    while(True):
        try:
            b_choice = int(input("Choose one of the 3: "))
            if 1 <= b_choice <= 3:
                break
            else:
                print("A number from 1-3")
        except ValueError:
            print("A number please. (1-3)")
    
    if b_choice == 1:
        slow_writting("Venture into the tomb...\n")
        contin()
        return 1
    if b_choice == 2:
        message = ("You decide to look at the pillars, it seems to be made out of a rich white stone. Marble you would think but you cannot be sure, as you look at each pillar, One crosses your eye as something gleams from its base.\n"
                   "You pick it up and look at the object. It seems to be a small red clay ball with some carvings and marks dotted all over it. The Akari speaks up.\n"
                   '"Ah, you found it, A life orb. These can save you from worse situations should they befall you.\n'
                   'You might be wondering why these items exist in the world for adventurers such as yourself to find.\n'
                   'Simply put, These were batteries for us Akari used to replenish our stocks.\n'
                   'I have been stockpiling a few so you may take that one and place it into the vessel I gave you."\n'
                   "You do as it says, and the thrum of life that erupts from it feels almost invigorating. With your new sense of strength, you instinctively head into the tomb.\n"
                   "Ready for anything.(Gain +1 Life!)\n"
                   f"Total: {life+1} lives.\n")
        cls()
        slow_writting(message)
        life_system(1)
        contin()
        return 1
    if b_choice == 3:
        print("Your curiosity gets the better of you, as you approach the Akari, it looks down, trying to face you.\n"
            '"I am confused, mortal."\n'
            'It speaks.\n'
            '"Do you not wish to venture deeper into the tomb… To find what you are looking for?"\n'
            'You nod but are curious about the being.\n'
            '"Well, I used to be known as Jerico. After the events of my master\'s demise, I stayed with him during his final moments, as he transferred my soul into the vessel you see before you.\n'
            'Making me an eternal guardian and protector of his home." He squats. "I am honored to have this role." He says, before standing up again.\n'
            '"Go, claim your treasure, before I change my mind."\n'
            'You nod, and head in. Enlightened by this experience.\n')
        contin
        return 1
################################################################################


# Setting/resetting global variables ###########################################
def globals():
    global father, life, name, nor
    father = 'Glaen'
    life = 3
    nor = 'nor'


# Life points give/take
def life_system(action):
    global life
    if action:
        life += 1
    else:
        life -= 1
        print("Wrong!")


# Placeholder
def lost():
    pass


# Text animation effect
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
    slow_writting("\tThe tomb of Akarak.")
    time.sleep(0.2)
    while name == '':
        name = input("\nEnter your name and let's get started: ")
    cls()


cls()
welcome_message()

while True:
    cls()
    globals()
    story_intro()

    while True:
        chc = input("Do you still want to continue?(y/n) ")
        if chc.lower() == 'y':
            input(f"Great. Remember, you only have {life} lives. Be careful.\nPress enter to continue...")
            break
        if chc.lower() == 'n':
            print("Bye...")
            exit()
        else:
            print("Type y for yes, n for no.")
    
    cls()

    # Checks for succ/fail puzzle.
    pass_1 = entry_room()
    pass_2 = False
    pass_3 = False
    pass_4 = False
    pass_5 = False
    pass_6 = False

    if pass_1:
        pass_2 = dung_room_1()
    if pass_2:
        pass_3 = dung_room_2()
    if pass_3:
        pass_4 = dung_room_3()
    if pass_4:
        pass_5 = dung_explore_4()
    if pass_5:
        input("Test input")