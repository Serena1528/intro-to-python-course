from urllib import request
from time import sleep
import winsound

url = 'https://www.google.com'
interval = 3

while True:
    print('checking if online...')
    try:
        # trying to connect to the URL
        request.urlopen(url)
        print('You are probably online')
        winsound.MessageBeep()
    except:
        print('You are probably offline')

    print(f'Sleeping for {interval} seconds...')
    print()
    sleep(interval)
