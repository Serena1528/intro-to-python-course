#list of movies
movies = ['Interstellar',
          'Spider-Man: Across the SpiderVerse',
          'Spider-Man: Into the SpiderVerse',
          'Spirited Away',
          'Fight Club']

#sorts the list alphabetically
movies.sort()

#reverses the list
movies.reverse()

#prints the movies sequentially
for movie in movies:
    print(movie)

#adds the lion king and the wolf of wall street to the list and prints the list
movies.append('The Lion King')
print(movies)
movies.append('The Wolf of Wall Street')
print(movies)

#gets the length of the list and prints the information
number_of_movies = len(movies)
print(f'You have {number_of_movies} movies in your list.')

#removes the lion king from the list
movies.remove('The Lion King')
print(movies)

#removes the first item from the list
first_movie = movies.pop(0)
print(movies)
print(first_movie)

#removes the last item in the list
movies.pop()
print(movies)

#removes fight club from the list
movies.remove('Fight Club')
print(movies)