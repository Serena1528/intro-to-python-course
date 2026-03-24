import time
import webbrowser
#attempts this first
isFinished = False
while not isFinished:
    try:
        seconds = int(input('Enter the number of seconds: '))
    except ValueError:
        print('Please enter a number!')

    mode = input('Do you want to play a video when done? ')
    url = 'https://www.youtube.com/watch?v=UG3VcCAlUgE'

    if seconds < 0:
        print('Please enter a positive number!')
    else:
        for i in range(seconds):
            time.sleep(i)
            print(f'{i+1},', end=' ')
        if mode.lower() == 'yes':
            webbrowser.open_new_tab(url)
            isFinished = True
        elif mode.lower() == 'no':
            print('Time is up!')
            isFinished = True
        else:
            print('Please enter a yes or a no! ')
