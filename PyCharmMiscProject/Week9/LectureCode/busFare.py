
#this function calculates the total expense of one specific fare type
def bus_ride_cost_calculator(fare_type):

    #asking for number of rides taken with the fare type
    number_of_rides = int(input(f'How many rides did you take while paying {fare_type} fares? '))

    #asking for the cost for the fare type
    bus_fare = float(input(f'What is the cost of one {fare_type} fare? $'))

    #fare cost * number of rides
    total_cost = bus_fare * number_of_rides

    print(f'You rode the bus {number_of_rides} and each ride costs ${bus_fare:.2f}')
    print(f'Your total {fare_type} cost is ${total_cost:.2f}')

    return total_cost

#the full function that will we run to make sure we calculate all possible fare types
def main():
    print('Bus fare calculator program')

    #formating so we run our previous function three times for regular fares, rush hour fares, and special discount ones
    total_regular_cost = bus_ride_cost_calculator('regular')
    total_rush_cost = bus_ride_cost_calculator('rush hour')
    total_special_cost = bus_ride_cost_calculator('special discount')

    #simple addition for the full cost
    full_cost = total_regular_cost + total_rush_cost + total_special_cost

    print(f'Your total bus expense is ${full_cost:.2f}')

#so we actually run main
main()