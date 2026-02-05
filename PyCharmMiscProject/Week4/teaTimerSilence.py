import time
import webbrowser
#attempts this first
try:
    seconds = int(input('Enter the number of seconds: '))
    mode = input('Do you want to play a video when done? ')
    url = 'https://www.youtube.com/watch?v=UG3VcCAlUgE'

    if seconds < 0:
        print('Please enter a positive number!')
    else:
        time.sleep(seconds)
        if mode.lower() == 'yes':
            webbrowser.open_new_tab(url)
        elif mode.lower() == 'no':
            print('Time is up!')
        else:
            print('Plese enter a yes or a no! ')



#if there is a ValueError then it prints this
except ValueError:
    print('Please enter a number!')