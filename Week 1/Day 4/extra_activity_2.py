import random

sum = 0
numbers = [
    random.randint(1, 100),
    random.randint(1, 100),
    random.randint(1, 100),
    random.randint(1, 100),
    random.randint(1, 100),
    random.randint(1, 100),
    random.randint(1, 100),
    random.randint(1, 100),
    random.randint(1, 100),
    random.randint(1, 100),
]

for i in range(0,len(numbers)):
    sum += numbers[i]

numbers.sort()
print(numbers)
print(sum)
if (sum % 2):
    print("Sum is odd.")
else:
    print("Sum is even.")