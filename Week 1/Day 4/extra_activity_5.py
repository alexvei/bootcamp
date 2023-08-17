

def find_numbers(listie):
    b_list = []
    for i in range(0, len(listie)):
        if 30 <= listie[i] <= 400:
            b_list.append(listie[i])
        else:
            pass

    return b_list

a_list = [3, 672, 89, 6, 35, 98, 491, 45, 513, 24]

print(find_numbers(a_list))
