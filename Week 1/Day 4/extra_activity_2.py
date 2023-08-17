import random

sum = 0
numbers = []

def oddeven(a_num):
    if (sum % 2):
        return "Sum is odd."
    else:
        return "Sum is even."


while (len(numbers)< 10):
    numbers.append(random.randint(1, 100))

for i in range(0,len(numbers)):
    sum += numbers[i]

numbers.sort()

print(numbers)
print(sum)

print(oddeven(sum))
