#gets user input to store the product name in the variable item_name
item_name = input('What is the product name? ')

#gets user input to store how many items were sold in the variable items_sold
items_sold = int(input('How many items were sold? '))

#gets user input to store the cost of one item and stores it in the variable unit_price
unit_price = float(input('How much does one item cost? '))

#calculates the total cost based on the quantity of items sold and the unit price
total = items_sold * unit_price

#adds a line beforehand for a cleaner visual effect
print()

#this chunk of code prints all the data with descriptions for the whole invoice
print(item_name + ' Sales')
print('Quantity sold: ' + str(items_sold))
print('Unit price: $' + str(unit_price))
print('Total: $' + str(total))