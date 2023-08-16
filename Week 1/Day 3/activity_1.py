order_count = 0

def take_order(topping, second_topping):
    global order_count
    print("Pizza with {} and {}.".format(topping, second_topping))
    order_count += 1

print(f'We have a total of {order_count} orders.')
take_order("pineapple", "ham")
print(f'We have a total of {order_count} orders.')