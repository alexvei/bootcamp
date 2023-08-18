# Write a function to take a parameter of a number, calculate all the square numbers (e.g. 2 x 2, 3 x 3) and return the sum of the squares
import random

def square(num):
    return num*num


def summing(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum


numbers_list = []
squared_list = []

for i in range(0, 10):
    numbers_list.append(random.randint(1, 10))
print(numbers_list)

for i in numbers_list:
    squared_list.append(square(i))
print(squared_list)

print(summing(squared_list))