age = int(input("Enter your age: "))
weight = int(input("Enter your weight, in pounds: "))
hasDonated = input('Have you donated blood before? ')
canDonate = 'You can donate blood!'
if hasDonated.lower() == 'yes' and age>= 16 and weight >= 120:
	print(canDonate)
elif hasDonated.lower() == 'no':
	daysDonated = int(input("How many days ago did you donate blood? "))
	if daysDonated > 56:
		print('You are not eligible to donate blood, you must wait' + str(int(56 - daysDonated)) + 'more days to donate blood!')
	else:
		print(canDonate)
else:
    print('You are not eligible to donate blood! You must be at least 16 and 110 lbs to donate!')