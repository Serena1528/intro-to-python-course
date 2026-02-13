import random

#a boolean to stop the loop when the program completes
wantToQuit = False

#will repeat until the program outputs the dice values and sets wantToQuit to true
while not wantToQuit:

    #makes sure that the user inputs an integer
    try:
        diceNum = int(input('How many dice to roll? '))

        #makes sure the user inputs a positive integer
        if diceNum < 1:
            print('Please enter a positive number!')

        #runs and finishes the program when the user inputs a positive integer
        else:
            print(f'about to roll {diceNum} dice.')
            for dice in range(diceNum):
                dice_value = random.randint(1, 6)
                print(f'Dice {dice+1} value is {dice_value}')
            wantToQuit = True
    except ValueError:
        print('Please enter a number!')