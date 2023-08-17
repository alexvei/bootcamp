print("This is a program that gives examples to some of the methods used with lists")
example_list = [
    "element 1",
    "element 2",
    "element 3",
    "element 4",
    "element 5"
]

print(f"The list is called 'example_list' and has the elements: {example_list}\n")
print("\t remove() method, removes an element from the list, say we want the last element removed, then it's example_list.remove(example_list[-1])")
example_list.remove(example_list[-1])
print(example_list)

print("\t reverse() method simply reverses the order of the elements in the list.")
example_list.reverse()
print(example_list)

print("\t sort() method sorts alphanumerically the elements in the list.")
example_list.sort()
print(example_list)

print("\t count(), gives the number of TIMES an element exists in the list.")
print(example_list.count(example_list[0]))

print("extend(), if we have a 2nd list, we can join the 2 lists together with this method.")
example_list_2 = [
    "element 7",
    "element 8"
]
example_list.extend(example_list_2)
print(example_list)