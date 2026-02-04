#asks the user to input how many cents they have
cents = int(input('How many cents do you have?'))

#determines if they have less than a dollar and prints the info
if cents < 100:
    print('you have less than a dollar')

#determins if they have more than a dollar and prints the info
elif cents > 100:
    print('you have more than a dollar')

#if they don't have more or less than a dollar, then they must have exactly a dollar, so this prints that info
else:
    print('you have exactly a dollar')