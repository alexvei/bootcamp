#A function takes two parameters – hours and minutes – return seconds

def seconds_converter(hours, minutes):
    hours_to_seconds = hours* 60*60
    minutes_to_seconds = minutes * 60
    total_seconds = hours_to_seconds + minutes_to_seconds
    return total_seconds

while True:
    try:
        hours = int(input("Enter hours: "))
        if 0 <= hours <= 24:
            break
        else:
            print("I need a number from 0 to 24.")
    except ValueError:
        print("Give me an integer.")

while True:
    try:
        minutes = int(input("Enter minutes: "))
        if 0 <= minutes <= 60:
            break
        else:
            print("I need a number from 0 to 60.")
    except ValueError:
        print("Give me an integer.")

print(f"Total seconds in {hours} and {minutes} are: {seconds_converter(hours, minutes)}.")
