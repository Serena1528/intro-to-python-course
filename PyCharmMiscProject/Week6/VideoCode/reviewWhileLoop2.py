keepGoing = True
while keepGoing:
    department = input('Please enter your 4 digit department code: ')
    if len(department) == 4:
        keepGoing = False
    else:
        print('Please enter a valid 4 digit department code')
