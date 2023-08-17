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

def string_converter(number_list):
    string_list = []
    for i in range(0, len(number_list)):
        string_list.append(f'{number_list[i]}')
    
    return string_list

converted_numbers = string_converter(numbers)
print(converted_numbers)