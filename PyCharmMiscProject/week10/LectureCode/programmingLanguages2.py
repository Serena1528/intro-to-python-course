import random
alice_languages = ['Swift', 'Kotlin']
bob_languages = ['HTML', 'JavaScript', 'CSS']

#combines and sorts the two lists of languages
team_languages = alice_languages + bob_languages
print(team_languages)
team_languages.sort()
print(team_languages)

#randomizes the combined list
random.shuffle(team_languages)
print(team_languages)