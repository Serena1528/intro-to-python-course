#asks the users age
age = int(input('What is your age? '))

#asks the users citizenship status
citizenship = int(input('How many years have you been a US citizen? '))

#asks where the user lives
stateLived = input('What state do you live in? ')

#asks where they want to be a senator
stateDesired = input('What state do you want to be a senator in? ')

#checks each variable and determins if they could legally be a senator
if citizenship >= 9 and age >= 30 and stateLived == stateDesired:
    print('You could be a senator!')

#if they do not fit each variable, this checks each individual one to see which one does not work
#this could be modified to more accurately display the information, as the program would stop after only 1 doesn't fit
elif citizenship < 9:
    print('You need to be a US citizen for at least 9 years to be a senator! ')
elif age <30:
    print('You need to be at least 30 years old to be a senator!')
elif stateLived != stateDesired:
    print('You need to live in the state you want to be a senator in! ')