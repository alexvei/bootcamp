

def only_e(the_list):
    b_list = []
    for i in range(0, len(the_list)):
        if 'e' in the_list[i]:
            b_list.append(the_list[i])
        else:
            pass
    
    return b_list


a_list = ["eyes", "nose", "mouth", "tongue", "head", "hair"]

print(only_e(a_list))