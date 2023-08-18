import random

rand_num = random.randint(0, 50)
my_num = 50
tries = 0

while rand_num != my_num:
    tries += 1
    print(rand_num)
    rand_num = random.randint(0, 50)

print(f"You've found {my_num} in {tries} tries.")