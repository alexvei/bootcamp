def words(a_list):
    b_list = []
    for word in a_list:
        b_list.append(word.count('e'))

    return b_list


the_list = ['detective',
            'handicap',
            'transfer',
            'nail',
            'haircut',
            'grudge',
            'pig',
            'portrait',
            'particle',
            'virus']

print("There's 10 words in the list. Letter 'e' appears:")
counted_e_list = words(the_list)

for i in range(len(the_list)):
    print(the_list[i], ':', counted_e_list[i])
