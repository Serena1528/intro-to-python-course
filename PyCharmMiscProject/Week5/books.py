booksNum = int(input('How many books to buy? '))
total = 0
for book in range(booksNum):
    book_price = float(input('Enter book price $'))
    if book_price == 0:
        print('Yay! Free book!')
    total += book_price
    total += book_price
print(f'The total price is {total}')