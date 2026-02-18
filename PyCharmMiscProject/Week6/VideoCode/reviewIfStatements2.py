houseTemp = input('Is your house warm or cool? (w/c) ')
houseShade = input('Does your house have sun or shade? (su/sh)')
if houseTemp.lower() == 'w':
    if houseShade.lower() == 'su':
        print('You should have a hibiscus plant!')
    else:
        print('You should have a Begonia plant!')
else:
    if houseShade.lower() == 'su':
        print('You should have a Jade plant!')
    else:
        print('You should have an Ivy plant!')