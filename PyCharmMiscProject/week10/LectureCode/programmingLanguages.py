#makes a list of different programming languages
languages = ['Python,'
             'Java',
             'JavaScript',
             'C#',
             'Swift',
             'Swift']

#removes the first instance of swift in the list

languages.remove('Swift')
print(languages)
#adds kotlin to the end of the list
languages.append('Kotlin')

#prints every item in languages
for language in languages:
    print(language)

#prints all the items in languages with a comma between them
all_languages = ', '.join(languages)
print(all_languages)

#sorts the languages alphabetically
languages.sort()
print(languages)

#reverses the list
languages.reverse()
print(languages)