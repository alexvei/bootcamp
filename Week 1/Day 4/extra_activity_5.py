def find_numbers(lista):
    b_list = []
    for i in range(0, len(lista)):
        if 30 <= lista[i] <= 400:
            b_list.append(lista[i])

    return b_list

a_list = [3, 672, 89, 6, 35, 98, 491, 45, 513, 24]

print(find_numbers(a_list))
