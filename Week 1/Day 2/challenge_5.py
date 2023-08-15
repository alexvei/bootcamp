time = 25
while(time > 24 or time < 0):
    time = int(input("Enter time (24hour format): "))
    if (time > 24 or time < 0):
        print("Enter a number between 0 and 24 please.")

place = ['work','gym','home']

if (time >= 9 and time <= 17):
    print(f"I'm at {place[0]}.")
elif (time > 17 and time < 19):
    print(f"I'm at the {place[1]}.")
else:
    print(f"I'm at {place[2]}.")