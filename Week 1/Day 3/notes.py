# space_1 = 'x'
# space_2 = 'x'
# space_3 = 'x'
# space_4 = 'o'
# space_5 = 'o'
# space_6 = 'o'
# space_7 = ' '
# space_8 = ' '
# space_9 = ' '

# print(f'{space_1}|{space_2}|{space_3}')
# print('------')
# print(f'{space_4}|{space_5}|{space_6}')
# print('------')
# print(f'{space_7}|{space_8}|{space_9}')

# if (space_1 == space_2 and space_1 == space_3 and space_3 == 'x'):
#     print("Player x won.")


# ==============================================================================
# water in kettle
# turn on kettle
# boil water
# pour water in mug
# place teabag in mug
# wait 2 minutes
# take teabag out
# (optional) sweetener
# (optional) milk
# ==============================================================================
def multiply_by_nine_fifths(celsius):
    return celsius * (9/5)

def get_fahrenheit(celsius):
    return multiply_by_nine_fifths(celsius) + 32

print("The temperature is {} F".format(get_fahrenheit(15)))

