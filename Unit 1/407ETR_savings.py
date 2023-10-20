"""
Author: Darrien Guan
Date: September 18, 2023
Description: This program calculates the cost of taking a local route and 407ETR route and time savings.
"""

# Global variable constants
HWY_SPEED = 100 # in km/h
LOCAL_SPEED = 60 # in km/h
HWY407_COST = 25 # in cents/km

def calculate_cost(hwy407_travelling_distance, local_travelling_distance, fuel_cost, local_traffic):
    '''Calculates the cost and duration of local and 407 trip.'''
    
    # Calculates 407 travel time in minutes, fuel costs in cents, toll fee in cents, and total 407 cost in cents.
    hwy_time = hwy407_travelling_distance*60/HWY_SPEED
    hwy_fuel_cost = (6.8*hwy407_travelling_distance)/100*fuel_cost
    hwy407_toll_fee = 1+hwy407_travelling_distance*HWY407_COST
    total_hwy407_cost = hwy_fuel_cost+hwy407_toll_fee

    # Calculates local route fuel cost and travel time for local route in minutes.
    local_fuel_cost = (8.8*local_travelling_distance*local_traffic)/100*fuel_cost
    local_time = local_traffic*local_travelling_distance*60/LOCAL_SPEED

    # Calls display_results function with corresponding arguments.
    display_results(total_hwy407_cost, local_fuel_cost, hwy_time, local_time)



def display_results(total_hwy407_cost, local_fuel_cost, hwy_time, local_time):
    '''Function displays the cost of hwy 407, local road, and time savings.'''

    # Displays calculating message
    print("Calculating the cost of travelling...")

    # Displays cost of local and 407 route with cents converted to dollars.
    print("The cost using 407ETR = %i dollars %i cents" % (total_hwy407_cost/100, (total_hwy407_cost%100)))
    print("The cost using local street = %i dollars %i cents" % (local_fuel_cost/100,(local_fuel_cost%100)))

    # Calculates the time difference between the local route and highway route, then displays it.
    time_difference = local_time - hwy_time

    # Prints time savings in hours if minutes is over 60.
    if time_difference >= 60:
        print("The time saving is %i hours and %i minutes." % (time_difference/60, time_difference%60))
    else:
        print("The time saving is %i minutes" % time_difference)

def main():
    '''Mainline logic'''

    # Gets user input for highway traveling distance, local traveling distance, fuel cost, and local traffic levels.
    hwy407_travelling_distance = float(input("Enter the travelling distance in km using 407: "))
    local_travelling_distance = float(input("Enter the travelling distance in km using the local street: "))
    fuel_cost = float(input("Enter the fuel cost per liter in cents: "))
    local_traffic = float(input("From 1 to 3, enter the level of local traffic (1 is normal, 3 is extremely busy): "))

    # Calls calculate_cost() function with corresponding arguments.
    calculate_cost(hwy407_travelling_distance,local_travelling_distance,fuel_cost,local_traffic)

main()