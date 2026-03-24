#a list of different streets in minneapolis
streets = ['Lake', 'Hennepin', 'Lyndale']

#prints the list
print(streets)

#prints individual elements of the list
print(streets[0])
print(streets[1])
print(streets[2])

#changes the first item, or lake, to chicago
streets[0] = 'Chicago'
print(streets)

#changes the different streets to other ones
streets[1] = 'University'
streets[2] = 'Washington'

print(streets)

#prints every item in streets
for street in streets:
    print(street)

delivery_instructions = 'Please deliver to these streets: '

#adds each street to the delivery_instructions string
for street in streets:
    delivery_instructions = delivery_instructions + street + ','
print(delivery_instructions)