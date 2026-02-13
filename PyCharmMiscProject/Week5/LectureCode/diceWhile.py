import random

wantToQuit = ''

while not wantToQuit:
    dice_value = random.randint(1, 6)
    print(f'You rolled a {dice_value}')
    wantToQuit = input('Press enter to continue. Press any other key to quit.')