import random
movies = ['Interstellar',
          'Spider-Man: Across the SpiderVerse',
          'Spider-Man: Into the SpiderVerse',
          'Spirited Away',
          'Fight Club']

#randomizes the list of movies
random.shuffle(movies)

#makes a numbered list of the randomized list
for num, movie in enumerate(movies):
    print(f'{num + 1}: {movie}')