import random

diceNum = int(input('How many dice to roll? '))

#print('about to roll ' + str(diceNum) + ' dice')
print(f'about to roll {diceNum} dice.')
for dice in range(diceNum):
    dice_value = random.randint(1, 6)
    print(f'Dice {dice+1} value is {dice_value}')
