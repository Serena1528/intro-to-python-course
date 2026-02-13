starId = input('Please enter your StarId: ')

while len(starId) != 8:
    print(f'ERROR: please enter a valid StarId. A valid StarId has to be 8 characters long')
    starId = input('Please enter your StarId: ')
print('Thank you, your StarId is ' + starId)