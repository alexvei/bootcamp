import random


def discount(discountee):
    disc = []
    disc.append(discountee * 0.1)
    disc.append(discountee-disc[0])
    return disc


def order(gds, prcs):
    global number_of_goods
    list_of_totals = []
    for i in range(number_of_goods):
        list_of_totals.append(gds[i]*prcs[i])

    return list_of_totals


def random_prices_list_gen():
    price = []
    for i in range(6):
        price.append(round(random.uniform(0,2), 2))
    
    return price


goods = ['eggs', 'butter', 'milk', 'peaches', 'oranges', 'apples']
order_list = []
total_list = []
prices = random_prices_list_gen()

total = 0
number_of_goods = len(goods)

for i in range(number_of_goods):
    print(f"{goods[i].capitalize():8} at £{prices[i]:3.3}.")

for i in range(0, number_of_goods):
    an_order = int(input("How many '{}' would you like? ".format(goods[i])))
    order_list.append(an_order)

total_list = order(order_list, prices)

print("Receipt: ")
for i in range(0, len(total_list)):
    print(f"{order_list[i]:3} x {goods[i]:8} ... {total_list[i]:3.3}")
    total += total_list[i]

print(f"Your total is £{total:3.3}.")

discount_list = discount(total)
print(f"Discount 10%: £{discount_list[0]:5.3f}.")
print(f"You pay: £{discount_list[1]:5.3f}")

 