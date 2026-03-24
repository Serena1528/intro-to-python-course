import random

#asks how many dice the user wants to roll and calls the roll_dice function to roll them.
def main():
    number_of_dice = int(input('How many dice to roll? '))

    roll_dice(number_of_dice)
    print('That was all the dice')

#gets a total number of dice to roll, then it will get a random number 1-6 number_of_dice times and will print the numbers
def roll_dice(number_of_dice):
    for dice_count in range(number_of_dice):
        dice_roll = random.randint(1, 6)
        print(f'The dice rolled a {dice_roll}')

#calls main()
main()