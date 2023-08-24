import os       # built-in python module for operating system commands
import random   # built-in python module for generating randoms
import sys      # built-in python module for more system stuff
import time     # built-in python module for time


################################################################################
# Global Variables 
name = ''
life = 3


################################################################################
# Systems/ functions
# Clear screen(cls), Contin(press enter to continue), 
# Explore question (continuation_choice), Exploration options, Life 
# System, Lose(lost), Text animation effect functions(slow_writting)
def cls():
    os.system('cls' if os.name=='nt' else 'clear')


def contin():
    input("Press enter to continue...")
    cls()


def continuation_choice():
    slow_writting("Do you wish to explore more?(y/n) \n")
    user_choice = input("Choice: ")
    cls()
    return True if user_choice.lower() == 'y' else False


def exploration_options(options_dict):
    print("You can:")
    for k, v in options_dict.items():
        print(f"\t"*k,f"{k}.{v}")

    while(True):
        try:
            if len(options_dict) != 1:
                b_choice = int(input("Choose one of the options: "))
            else:
                b_choice = int(input("Only one option left: "))
            if b_choice in options_dict:
                return b_choice
            else:
                print(f"A valid number.")
        except ValueError:
            print(f"A number please.")


def game():
    cls()
    global life
    life = 3
    logo()
    explore_entry_room_choices_dict = {1: "Venture into the tomb",
                                    2: "Look at the Pillars,",
                                    3: "Try to talk to the Akari."}
    
    explore_dung_room_choices = [{1: "Venture on.",
                                2: "Speak to the Akari.",
                                3: "Honor the dead.",
                                4: "Open a coffin."},

                                {1: "Venture deeper.",
                                2: "Look at the books on the table.",
                                3: "Examine the sigils."},

                                {1:"Continue deeper.",
                                2: "Speak to Akari.",
                                3: "Look for the key in the wardrobe.",
                                4: "Look for the key in the bed.",
                                5: "Pet the Akari."},

                                {1: "Approach the tablet.",
                                2: "Look into the large archway on the right.",
                                3: "Loot the place."}]

    welcome_message()
    story_intro()
    contin()

    if entry_room():
        rooms(explore_entry_room_message, explore_entry_room_choices_dict, 0)
    else:
        game()
    
    for index in range(0,4):
        if index == 3:
            if rooms(explore_dungeon_message[index], explore_dung_room_choices[index], index+1):
                puzzles(dungeon_room_messages[index], solutions[index], success_message_puzzle[index], fail_message_puzzle[index])
                break

        if puzzles(dungeon_room_messages[index], solutions[index], success_message_puzzle[index], fail_message_puzzle[index]):
            if not rooms(explore_dungeon_message[index], explore_dung_room_choices[index], index+1):
                game()
        else:
            game()
        
    for i in range(0, 3):
        if boulder(boulder_message[i], boulder_dictions[i], boulder_success_message[i], boulder_failure_message[i]):
            pass
        else:
            game()

    epilogue_story()
    

def life_system(action, question):
    global life
    if action:
        life += 1
    else:
        life -= 1
        if question:
            print("Wrong!")


def logo():
    print("_______              _______                                     /\    | /                   | /       ")
    print("   |    |___  ___       |    ___   _ _  |___     ___   ___      /__\   |/   ___    ___  ___  |/     ")
    print("   |    |   ||___|      |   |   | | | | |   |   |   | |        /    \  |\  |   |  |    |   | |\   ")
    print("   |    |   ||___       |   |___| | | | |___|   |___| |___    /      \ | \ |___\  |    |___\ | \   ")
    print("                                                      |                                            ")
    print("                                                      |                                               ")


def lost():
    contin()
    print("You are out of lives!")
    print("GAME OVER!")
    contin()


def slow_writting(word):
    for c in word:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0) ## 0 for debugging


################################################################################
# Dungeon Exploration
def rooms(message, dict, puzzle): 
    while True:
        slow_writting(message)
        player_choice = exploration_options(dict)
        all_exploration_list = [entry_room_explore_1_choices,
                                dung_explore_1_choices,
                                dung_explore_2_choices,
                                dung_explore_3_choices,
                                dung_explore_4_choices]
        cls()
        result = all_exploration_list[puzzle](player_choice)
        dict.pop(player_choice)
        if player_choice == 1 or not result:
            break
        if not continuation_choice():
            break 
    return result


def entry_room_explore_1_choices(chc):
    if chc == 1:
        slow_writting("Venture into the tomb...\n")
        contin()
        return True
    if chc == 2:
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
        life_system(1, 0)
        return True

    if chc == 3:
        print("Your curiosity gets the better of you, as you approach the Akari, it looks down, trying to face you.\n"
        '"I am confused, mortal."\n'
        'It speaks.\n'
        '"Do you not wish to venture deeper into the tomb… To find what you are looking for?"\n'
        'You nod but are curious about the being.\n'
        '"Well, I used to be known as Luke. After the events of my master\'s demise, I stayed with him during his final moments, as he transferred my soul into the vessel you see before you.\n'
        'Making me an eternal guardian and protector of his home." He squats. "I am honored to have this role." He says, before standing up again.\n'
        '"Go, claim your treasure, before I change my mind."\n'
        'You nod, and head in. Enlightened by this experience.\n')
        return True


def dung_explore_1_choices(chc):
    if chc == 1:
        message = ("You ignore the request of the Akari, venturing down into the darker depths.\n"
        "The Akari looks at the door you head towards. Sighing.\n"
        '"Perhaps another one will remember you all..."\n'
        "As it goes back to maintain the grim serenity within the walls...\n")
        slow_writting(message)
        return True

    if chc == 2:
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
        return True

    if chc == 3:
        message = ("You look towards one of the coffins, saying a prayer for them to wish them a blissful rest.\n"
        "The Akari sees this, shocked and happy. It walks up to you, extending its marble palm as you see an Orb of life.\n"
        "\"It is rare to see one so respectful of the past... you deserve to be rewarded. I hope this proves a lesson to you just as much as it did for me.\"\n"
        "You take the orb of life and place it into your vessel, it thrums with energies as you embrace it.\n"
        "The dead stand with you, as allies. Willing to retrieve you from whatever afterlife you find yourself in.\n"
        "You head towards the doorway, nodding in thanks towards the Akari before heading down. It waves as you do.\n\n")
        slow_writting(message)
        return True
    
    if chc == 4:
        cls()
        message = ("Your curiosity gets the better of you, as you see a coffin slightly open in the back that appears to have a glint of something.\n"
        "As you walk towards it, the Akari warns you. \"Do you so wish to throw away your life so willingly? Perhaps it is best for you to turn back.\""
        "You look at it disapprovingly, as you move the coffin. The denizen grabs you as it lurches out of the coffin.\n"
        "Dragging you in and closing it behind you. The Akari merely sighs. As it looks to your now floating spirit.\n"
        '"A shame... Perhaps it\'s best for your to remain here... till we can forge you a vessel for yourself..."\n\n')
        slow_writting(message)
        contin()
        print("You've died and have to start again.")
        contin()
        return False


def dung_explore_2_choices(chc): 
    if chc == 1:
        message = ("You realize how much effort that may come from examining everything in this room, and it has overwhelmed you.\n"
                "You decide a better use of your time is to venture on down into the depths.\n")
        
        slow_writting(message)
        contin()
        return True
    
    if chc == 2:
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
                "As you place the book down, you turn to the door, continuing on into the depths of the tomb…\n")

        slow_writting(message)
        return True 
          
    if chc == 3:
        message = ("You lean down towards the sigils, wanting to get a closer look, you aren\'t sure of the language of the runes that are on there but you notice something as you move pages out of the way of the full circle, a dulled out life orb.\n"
                "It seems weak but it has enough to keep you going in your adventure you think.\n"
                "As you place it into your vessel, it thrums weekly, the vessel begins to slowly empower it, reaching a level where it\'s as bright as the other Orbs that you have seen on your adventure.\n"
                "(Gain +1 Life!)\n"
                f"Total: {life+1} lives.\n"
                "With this, you head down to the depths, seeing what horors await you.\n")
        
        cls()
        slow_writting(message)
        life_system(1, 0)
        return True


def dung_explore_3_choices(chc):
    global life
    if chc == 1:
        slow_writting("The Akari clearly doesn't want to be bothered, and the box seems too malicious to be anything more than a trap,\n"
        "so you decide against your best judgment and venture down into the depths.\n"
        "Steeling yourself, for hopefully, the last time.\n")
        contin()
        return True
    
    if chc == 2:
        slow_writting("You aim to speak with the Akari, just before it sleeps, it looks up to you rather groggily, like a tavern patron the night after a crawl. It speaks.\n"
        "\"What is it mortal, my rest has been disturbed already by people like you, do not disrupt further...\"\n"
        "You ask what it is. It responds in kind.“I am an Akari, Fleming they used to call me in life.\n"
        "Sentience I was given after my master implanted my soul into here. I could learn to speak, write, read...\"\n" 
        "You ask what it was in a past life.\n"
        "\"I was a humble dog for Master Akarak, His best friend for when needed it.\n"
        "My body was so frail and so weak that he felt a connection with me specifically,\n" 
        "after he had rescued me from the deplorable streets of Aeisendrage,\n"
        "he took me here. Where he took care of me till I could wake no more…\"\n"
        "You seem... shocked and perplexed at this. Akarak was always told to you to be a cruel, unfeeling monster,\n"
        "yet with Fleming's existence it proves that he did care for things... Perhaps you were wrong to judge him harshly.\n"
        "You gain a new perspective onto this, leaving Flemming to his rest as it slumps down onto the bed.\n"
        "You head towards the stairs downward towards your final task.\n")
        return True

    if chc == 3:     
        slow_writting("""
            You think to look inside the wardrobe, seemingly to look around for any relevant information for that key,
            as you open the door.
            A skeleton falls out from it, forcing you to jump back as its bones crash against the floor.
            The Akari shoots up as well on its four legs. It walks over to you on the bed. “What are you doing Mortal?! 
            Why are you exploring my master’s private room?!” You point out the box on the side of the table 
            and talk about if you could open it.
            The Akari merely looks at you and growls, as it jumps at you. 
            Clearly it was not happy with that proposal as its strength and weight pin you down. 
            It starts to claw at you, bite you, till you are left bloody and bruised. 
            “Do not DARE to think about invading my master’s personal space… LEAVE!” 
            As you venture deeper, you have to use one of the life orbs in your vessel to 
            rejuvenate your strength as the wounds close over and bruises fade. 
            As the orb dimms to nothing remains.\n""") 
        life_system(0, 0)
        print(f"Lives left= {life}")
        if life == 0:
            slow_writting("""
            The damage is too much for you to continue, you slump down as all of your body hurts. 
            You notice as it begins to Petrify becoming that of stone. 
            You panic, but are ultimately too late to stop it, as you freeze in place, becoming a statue """)
            return False
        return True

    if chc == 4:
        slow_writting("""
        You are reminded of your father's antics with personal belongings, 
        you reach for the pillow case on the far right to avoid the Akari's ire. 
        You reach around within the Pillow till you find something cold, 
        you grab it and pull it out of the pillow case. 
        As a small red coin enters your sight. You wonder what it is for till you feel an urge to flip it.
        \nDo you?\n""")
        
        while True:
            user_choice = input("Yes or No: \n")
            if user_choice.lower() == "yes":
                cls()
                coin_sides = ["head", "tail"]
                while True:
                    user_side_choice = input("Head or Tail: ")
                    result = random.choice(coin_sides)
                    if user_side_choice.lower() in coin_sides:
                        slow_writting(f" \tAs you flip the coin it lands onto the {result}.\n")
                        if user_side_choice.lower() == result:
                            slow_writting("\tYou hear a small lock open. As the small lockbox raises its lid to reveal a Life orb."
                            "\tYou walk over and grab it, placing it into your vessel\n")

                            slow_writting("You get an extra life\n")
                            life_system(1, 0)
                            print(f"Lives left= {life}")
                            return True
                        else:
                            life_system(0, 0)
                            if life == 0:
                                lost()
                                return False
                            else:
                                print(f"Lives left= {life}.")
                                slow_writting("""You guess incorrectly, as the lockbox opens, 
                                tendrils of unknown origin steal a orb from your vessel, 
                                you feel as if the life was ripped from your body as you slump a bit.
                                Yet after a bit you come to. Noticing the lockbox has stolen your 
                                life orb and stored it away, luck was not on your side it seems...
                                You've lost life.
                                You place the coin back where you found it, and move on with the quest\n""")
                                return True
                    else:
                        print('Type "head" or "tail".')                

            elif user_choice.lower() == "no":
                cls()
                slow_writting("""You place the coin back where you found it, and move along with your quest.
                Already not wanting to test fate even more…\n""")
                break

            else:
                print("Type yes or no.")
                #players can't move past this point with the coin toss.
            
        return True
    

    if chc == 5:
        slow_writting("""
        You feel a weird urge to pet the Akari in front of you, it reminds you of a dog after all. 
        As you lower your hand onto its head and pet it. It seems shocked before looking towards you. 
        “...why did…” it states, confused. Before walking towards you and resting on your lap. 
        You give it more pets till it feels satisfied then continue on with its adventure. 
        The Akari thanks you before leaving.\n""")
        return True


def dung_explore_4_choices(chc):
    global life
    
    if chc == 1:
        return True
    
    if chc == 2:
        message = ("You look through the large archway, seemingly not seeing much beyond darkness.\n" 
                   "A small glint however shines through. As you walk towards it, you notice it's a life orb.\n"
                   "You pick it up and add it to your vessel.\n"
                   "Handy. (Gain +1 Life)\n"
                   f"Total Lives: {life+1}\n\n")
        cls()
        life_system(1, 0)
        slow_writting(message)
        contin()
        return True
    
    if chc == 3:
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
def boulder(message, dict, success_message, fail_message):
    global life
    cls()
    slow_writting(message)
    while True:
        print("You can:\n\t", end ="")
        for k, v in dict.items():
            print(f"{k}.{v}", end="\n\t")
        
        print(f"\t\tLives left: {life}")
        
        player_answer = input('Answer: ')
        if player_answer.upper() == "A":
                slow_writting(success_message)
                contin()
                return True
        elif player_answer.upper() == "B":
            life_system(0, 0)
            if life == 2:
                life_message = "You have 2 lifes left. Focus...\n"
                print(life_message)

            elif life == 1:
                last_life_message = "...This is Your last chance so think twice before You will answer...\n"
                print(last_life_message)

            elif not life:
                cls()
                slow_writting(fail_message)
                lost()
                return False
        
        elif len(dict) >= 3:
            if player_answer.upper() == "C":
                slow_writting(boulder_failure_message[-1])
                lost()
                contin()
                return False
        else:
            print("A or B only.")


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
    cls()
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
                life_system(0, 1)
                if life == 0:
                    print("Your heart is not pure, you will not survive. Leave this place and suffer the curse of Akarak!")
                    lost()
                    return False
        else:
            print("Type only A, B or C.")


def puzzles(message, answer, success_message, fail_message):
    global life
    cls()
    slow_writting(message)
    while True:
        print(f"Lives left: {life}")
        player_answer = input('Answer: ')
        if player_answer.lower() == answer:
                slow_writting(success_message)
                contin()
                return True
        else:
            life_system(0, 1)
            
            if life == 2:
                life_message = "You have 2 lifes left. Focus...\n"
                print(life_message)

            elif life == 1:
                last_life_message = "...This is Your last chance so think twice before You will answer...\n"
                print(last_life_message)

            elif life == 0:
                cls()
                slow_writting(fail_message)
                contin()
                return False


# Ending Story
def epilogue_story():
    escape_message = ("\tAs you stand up onto the flatland, you find your way back up the mountain, a staircase and a little bit of climbing allows you to reach the entryway of the tomb. The Akari looks to you.\n"
        "\t\"...Consider me shocked to see you succeed, you are worthy of Akarak's treasure.” You nod, looking at the staff on your back.\n"
        "\t\"The curse of Withering is dispelled by absorbing the necrotic energies back into the staff, by that point your father's body should be able to heal.\n\""
        "\tYou looked shocked, how did it know? You shrug as you realize these beasts are magical in nature and thank it for its aid.\n"
        "\tThe Akari nods and gestures to you to leave. You take that as a cue to leave as you run back towards your village, running into your father's house and attempting to cleanse him.\n")
    slow_writting(escape_message)
    contin()

    epilogue = ("\tAs you enter the home, you feel the pained wails of your father as you remember. It was never nice to deal with but you venture upstairs to where he lay.\n"
        "\tWith the knowledge you gained from Akarak's tomb and from the chase at the end, you siphon the energies of the curse on your father into Akarak's focus.\n"
        "\tHim finally resting peacefully, breathing slowly. As the pain seems to lighten from Glaen's body. You fall backwards, falling into a sitting position.\n"
        "\tSuccess... finally you think to yourself. I should keep this just in case someone else falls for the same issue... \n"
        "\tYou head back to your home after standing up, placing Akarak\'s focus into a display case as you clamber into bed. Resting after the exciting end of your adventure...\n\n")
    slow_writting(epilogue)
    contin()
    slow_writting("\t\tTHE END!\n\n\n\n\n")
    input("")


# Introduction story
def story_intro():
    message = ("Within the ruins of Akarak, lies an ancient and forgotten curse...\n"
    "Foolishly, your father Glaen sought out these riches within the Tomb of Akarak, a place\n"
    "feared and known for being a perilous journey of twisting corridors\n"
    "and mind-boggling riddles. Glaen failed to escape with the treasure, having to\n"
    "leave it behind to save their own life, Akarak's lingering will curse them\n"
    "to a fate worth that death. Immortality, but endless pain. They have been\n"
    "bedridden ever since and have lost themselves in their own torment.\n")

    message_two = (f"You are {name.capitalize()}, You are the child of Glaen.\n" 
    "He is suffering from the curse of Akarak, writhing in pain and anguish as it slowly eats away at them, consuming their flesh and soul into nothing more than a mindless husk.\n" 
    "You began to search for answers, solutions, anything to help your father out to not see home rite and wither away into a shambling mound of madness.\n" 
    "A traveling old hermit visited your village of Ransburg, hailing themselves as an ex-disciple of Akarak.\n"
    "She was named Nor, you asked for her aid, mention the situation with your father.\n"
    "Nor pondered this, examining Glaen before telling you the way to save Glaen is by delving into the tomb yourself\n" 
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


# Answers
solutions = [ 'death',
            'nor',
            'souls',
            'wake']

# Messages
dungeon_room_messages = [("As you enter the tomb...\n"
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
    "\tI am everyone's finale fate.\n"),
     ("As you hop off the last step, you are left with what appears to be a rundown Ritual room.\n"
    "Books and tomes scatter the floor as bookcases seem to have toppled upon themselves.\n"
    "You can climb through some of the passageways created by the toppled bookshelves and reach a pedestal.\n"
    "There sits a book, with a bookmarked page.\n"
    "You open the book to the page and see it written in fine ink.\n"
    '"To those that read this and are not of my troupe, I ask this of you, around this room are the remnants of my study. Where I practiced my forbidden magics and held my darkest secrets,\n'
    'for whatever reason you chose to venture into this sacred place, I ask this of you. Who is the disciple I sent off to the realm of the living,\n'
    'to explore and learn more about life and death?"\n\n'),
    ("Venturing deeper into the tomb, you happen upon Akarak's chambers, Gathering dust and seemingly destroyed...\n"
    "\tYou examine more and more of the room and notice the indent in the wall opposite the door you came from.\n"
    "\tIt was then you heard a noise upon the destroyed and dusty bed.\n" 
    "\tAn Akari, a small one. About the size of a puppy, it looks up to you and speaks.\n"
    "\t\"This place has seen better days, yet here used to be Akarak\'s room a place where he often sought refuge and peace from the troubles of training more acolytes.\"\n"
    "\tYou looked at it shocked, asking about why Akarak seems so... misunderstood...\n" 
    "\tThe Akari replied. \"Akarak was our master, he cared for us all, he cared little for affairs beyond that.He was defensive and isolated.\n"
    "\t Akarak fought so that all of us folks who didn't fit in belonged, do you understand?\"\n"
    "\t\"We ask this of you then, what are we made of aside from stone...What powers us forward?\"\n"),
    ("As you approach the tablet, you see a riddle written on it.\n"
    "\"Throughout your journey down in my depths, you have learnt more of my presence in the world. My motives and my treatment of others. Now I ask this of you, outsider.\n"
    "Fill in the word below the tablet, and it shall allow you into my focus.\"\n"
    "Below you see every single letter of the alphabet placed down in a chest. Fitting perfectly towards the tablet. What will you spell?\n\n")]

# Success Messages
success_message_puzzle = [("\tYour memory is sharp, I implore you to venture on.\n"
    "\tBut you may pay respects to those who have fallen before you, they rest within these halls.\n"
    "\tPerhaps they will give you the strength and courage to venture deeper into our master abode.\n"),
    
    ('"\tNor... yes... I do miss her... I trust she is finding your realm suitable...\n'
    "\tI implore you to venture deeper, you seem wiser than the rest...\n"
    "\tYet if you wish to learn more, read some of the books on this table...\"\n"),

    ("\"Yes... the souls of those who fell to the teachings.Akarak mourned for them. \n"
    "Stored their souls away within these. Akari, venture on adventurer, you are close to the end...\"\n"),

    ("The walls rumble as the wall behind the tablet raises. Showing a staff of malicious energies.\n" 
    "Akarak's focus.\n" 
    "You take it, and venture outwards, seemingly conquering the challenges.\n")]

# Fail Messages
fail_message_puzzle = [("You do not know? Perhaps I shall show you!\n"
    "As it shouts, the coffins burst open and fleshless beings erupt from them.\n" 
    "You are surrounded, with no hope to escape as the door shuts behind you.\n"
    '\"You will share the fate of these people... as many others have before\"\n'
    "As the skeletons shove you into a new coffin. And etch your name onto the front.\n\n"),

    ("You have failed to answer the question correctly in three attempts.\n"
    "The book closes on you, the doors closing and leaving you trapped.\n"
    "The sigils of the room light up as necrotic energy primates through the air.\n"
    "You feel yourself slowly wither, as you watch as the spirit of Akarak guides you to the next life.\n"),

    ("The small Akari merely looks at you. \"Perhaps you should learn...\"\n"
    "As you feel your soul ripped from your body, it floats around. And floats towards a human sized Akari,\n" 
    "your soul is dragged in, as you now possess a stone body," 
    "you can do no more, only remain vigil over this place... till another adventure challenges your master.\n"),

    ("You hear a large opening of the coffin behind you, this shriveled corpse steps out and looks at you.\n" 
    "It speaks slowly.\n"
    "\"You… have… learnt… NOTHING!\"\n" 
    "As the corpse lashes out, grabbing you with lightning speed and pulling you into its resting place.\n" 
    "The top of the coffin sliding on top as you are trapped in Akarak's tomb.\n")]

# Explore messages
explore_entry_room_message = ("\tThe Akari stands back and lets you gather your surroundings.\n"
    "You stand at the base of the tomb, it stands tall as it's in the base of a large mountain, the tomb's door is circular as it rolls sideways to allow you to enter the tomb.\n"
    "Two pillars stand broken at the entryway, the rubble spreading across the stone path.\n"
    "The Akari stands leaning against the wall.\n"
    "Its figure is so tall that you have to lean your neck upwards to see its head. It looks like a stone lion as it merely watches you, it doesn't appear like it wants to talk.\n\n")

explore_dungeon_message = [("As the far side tomb door raises up, you are left with a room with the Akari and the tombstones and coffins dotted about this place.\n"
    "You wonder what the usage for those were, who the people are inside the coffins and what they did for their master...\n"
    "The room is rather dark and murky, dirt and muck being on some of the coffins as dust covers the entire floor, most of the tombstones are smudged beyond belief apart from a few.\n"
    "The Akari goes back to cleaning and maintaining the tombstones, seemingly dysfunctional for a while till you came and opened the place up again.\n"
    'The Akari speaks. "Pay respects to the dead while you are here... perhaps it will gain you favor among our gods and Akarak.".\n\n'),

    ("As the trial is complete in this room, you look around the entire room. Trying to glean what you can.\n"
    "The floor is in absolute chaos as books and tomes litter the floor, multiple pages ripped out lie next to them, all from differing volumes.\n"
    "The bookshelves seem precariously balanced off each other, if it were to move even just a tiny bit, they could collapse and cause serious damage to this entire room. \n"
    "After you move some of the books and pages, you see necromantic sigils that seem innate.\n"
    "What do you do?\n"), 

    ("As you look towards the rest of the room after the puzzle was completed you are left to explore Akarak's person chamber."
    "\nWithin this room contains a bed, multiple sets of drawers all of varying amounts of stability, a wardrobe and a bedside table.\n"
    "You look around at all the furniture that has been ultimately destroyed or covered with dust and rubble.\n"
    "The Akari merely lounges back onto the bed. Contempt with the puzzle it gave you and aims to rest.\n"
    "As you search through a few of the different drawers and wardrobes, you find a lockbox with a black sigil on it.\n"
    "Unsure of what it is, you leave it on the side till you can find a small key for it somewhere within the room.\n"),

    ("Finally, you arrive at the depths of Akarak's tomb.\n"
    "A wide open room with a large entry way on both the left and right of the room stands tall.\n"
    "You notice a large stone coffin in the middle of the room.\n" 
    "You steel yourself, approaching the coffin and reading it.\n"
    "\"Akarak, The abandoned lich\" it read.\n" 
    "Your eyes scan the room around you again, from the middle,\n"
    "you see a stone tablet on the opposite side of the entryway with empty holes.\n\n")]

# Boulder dictionaries
boulder_dictions = [ 
    {"A": "\"Walk the balance beam\"",
    "B": "\"Jump\""},

    {"A": "Hide in the corner",
    "B": "\"Run for it!\""},

    {"A": "Use the focus of Akarak",
    "B": "\"Look for a hiding spot!\"",
    "C": "Push the boulder."}]

# Boulder Messages
boulder_message = [
    ("As you grab the focus, you feel its power course through you.\n"
    "This is what you need to save your Father.\n"
    "\tYou move out of the indent in the wall and head towards the doorway, However. The original entrance to the treasure room has closed behind you.\n"
    "\tConfused, you look around as your attention is brought to the large gates. As you peek through, you hear a distant rumbling…\n" 
    "\tThere\'s a bit of time before you realize a final trap has been placed, as a boulder lands in the door in front of you. You have to make a mad dash towards the exit now! Quickly run!\n"
    "\tAs you run through the massive entryway, you realize it\'s a straight shot out to the other side of the mountain, traps and pits litter the way as paths converge and change.\n"
    "\tThe twisting corridors and turning caverns throw you out to a pit of spikes.\n"
    "\tA small balance beam stands in front of you. The boulder crashes into the wall behind you, giving you a chance to think about your next move.\n"
    "\tWhat will you do? The Pit looks like you can make it if you jump.\n"),

    ("\tAs you make your way towards the next challenge, you dash and slide towards dimly lit hallways as you find yourself walking into a small hallway.\n", 
    "\tAs you walk towards the entryway of the thin hallway, a necrotic bolt flies past you,\n" 
    "\tLanding directly onto the wall behind you, you manage to avoid it but realize that you may have to risk it and make a dash towards the end.\n"
    "\tYou also notice a gap small enough for you to hide into, deep enough to protect you and the focus from the boulder.\n" 
    "\tAfter you wave your hand in front of the same gap that shot the bolt, you notice it can only fire one bolt before needing to recharge.\n"
    "\tWhat will you do?"),

    ("\tThe final puzzle presents itself, the boulder blocking your way is the only thing between you and the way to save your father is a large spherical rock.\n", 
    "\t You have a few options after examination of the current hallway. The focus thrums on your back as you could possibly use it… somehow.\n" 
    "\tJudging by what you know of Akarak, perhaps there are some spirits willing to provide you aid if you were to channel your energies into it… but you wouldn\'t know the cost of tapping into Akaraks own magic.\n"
    "\tYou could attempt to look for a hiding spot and wait for the other boulder you believe is coming after this one to push it out of the hole yet that could risk you getting trapped between the stack of boulders.\n" 
    "\tFinally, you could always throw everything to the wind and push the boulder with all your might. Perhaps it might be enough to free yourself from the prison of cave systems.n"
    "\tWhat will you do?")]

# Boulder Success Messages
boulder_success_message = [
    ("\tYou decide to play it safe, slowly advancing over the balance beam while the boulder slowly picks up momentum behind you. \n"
    "\tThankfully, the wall crash managed to give you enough time to safely get across. You take a breath before running, the boulder falling into the pit and destroying the beam.\n"
    "\tYou walk slowly ahead before you hear a familiar crashing sound. As another boulder crashes to the wall behind you. Safe to say you need to pick up the pace! As there may be more behind you!.\n"),

    ("\tYou decide to play it safe again, clambering into the corner and hiding while the boulder rumbles past you. \n"
    "\t You hear the bolts of necrotic energy blast out from what you assume are crystals as they all blast against the wall.\n"
    "\tYou peek out and start walking towards the doorway, none of the bolts firing at you as their energy dims.\n"
    "\tYou make your way towards the exit, finding the boulder blocking the doorway.\n"
    "\tYou can see light try and reach through the sides of the boulder, the exit! You're almost there."),

    ("\tWith what you know of Akarak\'s magics, you attempt to channel whatever magical affinity you have into the focus.\n"
    "\tThe dim light hums as it shoots a beam of necrotic energy to the ground,\n"
    "\tRaising the unlucky adventurers of the past from the ground, you looked shocked but explained to them your peril. They agree to help you, only to be free from this accursed place.\n"
    "\tYou accept as you and the skeletons push against the boulder, doing enough to push the boulder free it falls into the river below,\n"
    "\tthe path thankfully leads to the left, opening to a piece of flatland that allows you to roll over and land on your back.\n"
    "\tYou did it! You managed to escape with the focus, while gaining some understanding about the focus and how to wield it.")]

# Boulder Failure Messages
boulder_failure_message = [
    ("\tTime is against you, you don't have time to cross a rickety beam.\n" 
    "\tYou run back, and try to make a jump for it. \n"
    "\tAs you fly through the air, the boulder picks up the momentum and starts to roll behind you, that throws off your landing as the loud crashing causes you to recoil from the sound.\n"
    "\tAs you land, you wobble unsteadily as you land on the edge and topple behind, falling into the pit.\n" 
    "\tYou land with a thud as the boulder crushes you and the focus. Dooming your father to his withering undeath."),
        
    ("\tTime is against you! You have to MOVE! You dash through the gauntlet of crystals as the last one hits your leg.\n" 
    "\tYou wince in pain but have to push through, seeing the light at the end of the tunnel.\n"
    "\tAs you keep moving, you feel the necrotic energies pulse through your leg, making you have to limp\n"
    "\tAs you approach the entryway, your right leg is fully numb, and you can't stand up straight.\n" 
    "\tTumbling to the floor as the focus falls in front of you. The roaring of the boulder coming crashing down, it rolling over you and getting trapped within the door."),

    ("\tYou examine the hallway again, you see a small crevice that is enough to fit you, but not the focus. \n"
    "\tRealizing the issues that come with leaving the focus behind, you have to accept that this is not possible, the boulder crashing behind you as you keep looking.\n"
    "\t It rolls against the walls and catches up, you have no choice, you dive for the hole from before, getting as much of the focus in as you can but it snaps in half as the boulder crashes against the other boulder.\n"
    "\t Only making a bigger pile of boulders. You hear Akarak\'s voice. \"Another failure… another corpse...\" as you instantly feel your body wither way, much like your father\'s you note. As you are trapped into a small tomb for yourself, forever."),

    ("\tYou steel your nerves and push against the boulder, using all your strength to attempt to dislodge the boulder.\n" 
    "\tThe muscles in your body screaming to not strain yourself but you press on, to no avail\n"
    "\tThe boulder crashes behind you, as you try even harder but fail as the boulder crashes into you, flattening you and crushing the focus. Dooming both you and your father...\n")]

game()