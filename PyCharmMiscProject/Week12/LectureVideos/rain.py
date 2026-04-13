months = ['June', 'July', 'August']

rainfall_per_month = {}

#gets user input and adds it to the dictionary for the rain
for month in months:
    rain = float(input(f'How much rain fell in {month}? '))
    rainfall_per_month[month] = rain

print(rainfall_per_month)

#prints the data in the dictionary
for month, rain in months.items():
    print(f'In {month} it rained {rain} inches')

#gets the total rainfall
total = sum(rainfall_per_month.values())
print(f'The total rain is {total} inches')

#gets the average rainfall
number_of_months = len(rainfall_per_month)
average = total / number_of_months
print(f'The average for {number_of_months} months is {average} inches')