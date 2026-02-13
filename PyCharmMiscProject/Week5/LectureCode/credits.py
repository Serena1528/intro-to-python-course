creditsNum = int(input('How many credits are you taking this semester? '))

while creditsNum < 0:
    print('ERROR: Please enter a positive integer!')
    creditsNum = int(input('How many credits are you taking this semester? '))

if creditsNum >= 12:
    print('You are a full time student')
elif creditsNum >= 6:
    print('You are a half time student')
else:
    print('You are a less than half time student')