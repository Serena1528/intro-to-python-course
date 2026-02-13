total = 0
moreBooks= True
while moreBooks:
    bookPrice = float(input('Please enter your book price $'))
    total = total + bookPrice
    anyMore = input('Would you like to enter more books? (y/n) ')
    if anyMore.lower() == 'n':
        moreBooks = False

print(f'The total of all the books is ${total}')