import time
import webbrowser
#attempts this first
try:
    seconds = int(input('Enter the number of seconds: '))

    if seconds < 0:
        print('Please enter a positive number!')
    else:
        time.sleep(seconds)
        print('Time is up!')


#if there is a ValueError then it prints this
except ValueError:
    print('Please enter a number!')