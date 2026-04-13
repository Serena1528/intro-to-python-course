movies = {
    'Spiderman: Across the Spiderverse': 8,
    'The Wolf of Wall Street': 7,
    'Interstellar': 10,
    'Batman': 9
}

print(movies)

#gets a specific score
spiderman_score = movies['Spiderman: Across the Spiderverse']
print(spiderman_score)

#changes the value of interstellar
movies['Interstellar'] = 9
print(movies)

#adds a new item
movies['Barbie'] = 8
print(movies)

#testing a score that doesnt exist
batman_score = movies['Batman']
print(batman_score)

#tests an if statement for a score that doesnt exist
if batman_score is None:
    print('No batman found')
else:
    print(f'There is a rating for batman and it is {batman_score}')

#prints each movie and its rating
for movie in movies:
    rating = movies[movie]
    print(movie)
    print(rating)

#prints each movie and its rating, but better
for movie, rating in movies.items():
    print(f'{movie} has a rating of {rating} out of 10')

#removes and item
movies.pop('Batman')
print(movies)