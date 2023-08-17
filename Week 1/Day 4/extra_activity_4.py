def list_of_numbers(the_list):
    another_list = []
    for i in range(0,len(the_list)):
        another_list.append(the_list[i]*2)
        another_list.append(the_list[i]/2)
        another_list.append(the_list[i]*4)

    return another_list



a_list = [3, 10, 24]
print(list_of_numbers(a_list))