quiz_scores = {
    'Al': [8, 9, 5],
    'Bettina': [6, 10, 10],
    'Cody': [7, 7, 9]
}

#prints each students scores
for student, list_of_scores in quiz_scores.items():
    print(f'Student {student} has scores {list_of_scores}')

#gets the list of cody's score
cody_scores = quiz_scores['Cody']

#prints each score and which quiz cody got it on
for i, score in enumerate(cody_scores):
    print(f'On quiz {i+1} Cody scored {score}')

#prints cody's max score
cody_max = max(cody_scores)

#prints bettina's lowest score
bet_scores = quiz_scores['Bettina']
bettina_min = min(bet_scores)