#makes a list of quiz scores
quizScores = [0] * 5

print(quizScores)

#adds scores for each quiz with user input
for quiz, score in enumerate(quizScores):
    new_score = int(input(f'Enter your score for quiz {quiz+1}: '))
    quizScores[quiz] = new_score

print('Your scores are:')
print(quizScores)