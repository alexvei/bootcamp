import random

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

numbers.sort()
print(numbers)
print(f"The difference between the largest ({numbers[-1]}) and" 
      f"the smallest ({numbers[0]}) number: "
      f"{numbers[-1]-numbers[0]}")