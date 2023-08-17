import random


def string_converter(number_list):
    string_list = []
    for i in range(0, len(number_list)):
        string_list.append(f'{number_list[i]}')
    
    return string_list

numbers = []
while (len(numbers)< 10):
    numbers.append(random.randint(1, 100))

print(f"Integers list: {numbers}")
converted_numbers = string_converter(numbers)
print(f"Strings list: {converted_numbers}")