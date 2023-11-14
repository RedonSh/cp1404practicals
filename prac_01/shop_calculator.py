items = 0
price = 0

items_number = int(input("Number of items: "))
for i in range(items_number):
    item_price = float(input("price of item "))
    price += item_price

if price > 100:
    price *= 0.9

print(f"Total price for {items_number} items is {price}")