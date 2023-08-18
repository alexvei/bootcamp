#In a function, accept a list of numbers.  Convert numbers in a list to the correct number of dashes.  Return a list of dashes.  Print the list of dashes.
import random
def dash_converter(a_list):
    dashes = []
    for i in a_list:
        dashes.append('-'*i)
    
    return dashes

num_list = []
for i in range(0, 10):
    num_list.append(random.randint(1, 10))

dashes_list = dash_converter(num_list)
print(num_list)
print(dashes_list)