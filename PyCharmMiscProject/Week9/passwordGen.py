# Example program: random password generator where the user can enter the
# length of the password they want, for example 8 or 12 characters,
# and the program generates a random password of that length.

import string
import random
# control the other functions - manage the order that the functions are used in
# defining a function - this doesn't run automatically
def main():
    characters = make_list_of_characters()
    length = get_password_length()
    password = generate_password(characters, length)
    display_password(password)

def make_list_of_characters(): # Task 1 - identify characters to choose from in the password
    letters = string.ascii_letters
    print(letters)
    return letters  # output those characters

# Task 2 - ask user how long password should be (and optionally validate)
def get_password_length():
    password_length = int(input('Enter password length: ')) # optional validation
    return password_length  # output password length entered

# Task 3 - generate password, using the characters to choose from AND the length of the password
def generate_password(letters, password_length):
    password = ''  # start with empty string
    for letter in range(password_length): # repeat once for each letter needed
        random_letter = random.choice(letters)
        print(random_letter)
        password = password + random_letter
    return password  # output password

def display_password(password): # Task 4 - display password
    print('Your password is: ' + password)

main()  # call main function