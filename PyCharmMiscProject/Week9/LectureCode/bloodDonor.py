#asks for the users age and weight and calls check_donor_eligiblity to determine if they can donate blood
def main():
    age = int(input('What is your age?'))
    weight = int(input('What is your weight, in lbs?'))
    eligible = check_donor_eligibility(age, weight)
    if eligible:
        print('You are eligible')
    else:
        print('You are not eligible')

#checks if the user is at least 110lbs and 17 years old and returns true if they are, otherwise returns false
def check_donor_eligibility(age, weight):
    if age >= 17 and weight >= 110:
        return True
    else:
        return False

#calls main
main()