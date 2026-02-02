item_name = input('What is the product name? ')

items_sold = int(input('How many items were sold? '))

unit_price = float(input('How much does one item cost? '))

total = items_sold * unit_price

print()
print(item_name + ' Sales')
print('Quantity sold: ' + str(items_sold))
print('Unit price: $' + str(unit_price))
print('Total: $' + str(total))