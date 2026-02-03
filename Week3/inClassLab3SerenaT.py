#assigns the string 'Water calculator' to  the variable program_name
program_name = 'Water calculator'

#the = assigns the integer 10 to the variable water_to_drink
water_to_drink = 10

#the print function outputs data to the terminal, with quotes it prints the string
print('Welcome to the ' + program_name)

#try/except statement allows to show the end user what they are doing wrong, the "try:" is what happens first
#and the "except:" is what happens after, if a given error happens.
try:
    #takes an integer input and assigns it to the variable
    glasses_drunk = int(input('How many glasses did you drink today? '))

    #this top level if/else statement allows to show the end user if they accidentally input a negative number
    #which wouldn't be caught by the try/except statement
    if glasses_drunk > 0:
        glasses_to_drink = water_to_drink - glasses_drunk

        #this if statement allows us to display to the end user if they have reached the threshold for how much
        #water they need to drink
        if glasses_to_drink <= 0:
            print('You drank all the water you need today!')
        else:
            print('You need to drink ' + str(glasses_to_drink) + ' more glasses today!')

    else:
        print('Please enter a positive number!')


except ValueError:
    print('Please enter a whole number!')