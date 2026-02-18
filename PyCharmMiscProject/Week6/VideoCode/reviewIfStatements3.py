teamOneScore = int(input("Enter team 1's score:"))
teamTwoScore = int(input("Enter team 2's score:"))
if teamOneScore > teamTwoScore:
    print('Team 1 wins')
elif teamTwoScore > teamOneScore:
    print('Team 2 wins')
else:
    print('It was a tie')