table_list = []

def multi_table(num):
    global table_list
    product = 0
    a_list = []
    for i in range(1,13):
        product = num * i
        a_list.append(product)
        
    table_list.append(a_list)


for i in range(1, 13):
    multi_table(i)

for i in range(1, 13):
    print(f'{i:3} Table  ', end= '|')

print('')
for j in range(0, 12):
    for i in range(0, 12):
        print(f"{j+1:3}x{i+1:2}= {table_list[j][i]:3}|", end= '')
    print('')


