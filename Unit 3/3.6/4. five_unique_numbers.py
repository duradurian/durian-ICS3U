"""
Author: Darrien Guan
Date: Oct 24
Discription: Asks user for 5 numbers, doesn't stop until 5 unique numbers entered.
"""

def main():

    # Unique numbers list.
    numbers_list = []

    while True:
        number_input = int(input("Enter an integer: "))

        existing = 0

        # checks each number for matches.
        for i in numbers_list:
            if i == number_input:
                existing = 1
            else: existing = 0

        # If not matches, input num is inserted into numbers list.23

        if existing == 0:
            numbers_list.append(number_input)
        
        # Ends loop once there are over 5 numbers.
        if len(numbers_list) == 5:
            break

    # Display results.
    print(numbers_list)

main()