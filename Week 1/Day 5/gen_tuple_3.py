import random


def adding_val(value):
    global chosen_chord
    print(f"New chord - {chosen_chord}{value}")



basic_chords = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
rand_chord = random.randint(0,len(basic_chords)-1)
chosen_chord = basic_chords[rand_chord]
print(f"Basic Guitar Chord - {chosen_chord}")


detail = input("Added detail - ")
adding_val(detail)