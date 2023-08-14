print("This program gives an example for each of the methods below:")
print("upper(), lower(), capitalize(), count(), find(), replace(), strip().\n")
example_sentence = "This is the example sentence."
print(f"{example_sentence}")

print("\n>upper() capitalizes every letter in a string.")
print("\t", example_sentence.upper())

print("\n>lower() lowercases every letter in a string.")
print("\t", example_sentence.lower())

print("\n>capitalize() capitalizes the first letter in a string and rest into lowercase.")
example = "wORd"
print(f"\t The {example} turns into {example.capitalize()}.")

print("\n>count() takes a letter as an argument and it counts how many times that letter appears in the string.")
print(f"\t There is/are {example_sentence.count('a')} letter 'a' in the example sentence.")

print("\n>find() simply finds the PLACE in the string, where the letter, given as an argument, is placed at.")
print(f"\t The letter 'a' is at place {example_sentence.find('a')} of the string.\n\t And we can check that this is true by using 'example_sentence[14]' : {example_sentence[14]}")

print("\n>replace() simply replaces a character in a string with a different character, given as an argument.")
print("\t", example_sentence.replace("a", "b"))

print("\n>strip(), just removes the whitespace in a string.")
example_2 = '    word    '
print(f"\tSay we have the string '{example_2}'.")
print(f"\tIt becomes '{example_2.strip()}'.")
