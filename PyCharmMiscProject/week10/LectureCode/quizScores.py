"""Changing a list item"""

#list of scores
quiz_scores = [8,4,10,9,7]
quiz_scores[1] = 10
print(quiz_scores)

#asks for which quiz to modify
quiz = int(input('What quiz did you retake? '))

#adjusts the given number to index properly because computers count from 0
index = quiz - 1

#asks for adjusted score
score = int(input(f'What was your score on quiz {quiz}? '))

#adjusts the given score in the proper index
quiz_scores[index] = score
print(quiz_scores)