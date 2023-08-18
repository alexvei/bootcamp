import random

i = 0
div_seven = []
while i != 6:
    var = random.randint(1, 30)
    print(var)
    if var % 7:
        pass
    else:
        div_seven.append(var)
    i += 1

print(div_seven)