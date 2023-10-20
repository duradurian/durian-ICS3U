"""
Author: Darrien Guan
Date: September 29, 2023
Description: Computer guesses user input number using classic serach algorithm.
"""

# GLOBAL CONSTANTS
MAX_NUM = 100
MIN_NUM = 1

def main():
    '''mainline logic'''
    
    repeat_stat = 0
    
    # Triple nested while loops. First one starts a game, second and third one are within a game.
    while True:

        # Breaks loop if repeat_stat is 1
        if repeat_stat == 1:
            break
            
        user_input_number = int(input("Enter an integer from 1 to 100: "))
        repeat_stat = 0
        
        while True:
            
            # Breaks loop if repeat_stat is 1
            if repeat_stat == 1:
                break

            if repeat_stat == 2:
                break
            
            # guesser min and max variables.
            computer_min = MIN_NUM
            computer_max = MAX_NUM
            
            while True:
                
                # Always guesses the median (rounded) of computer_min and computer_max. It will progressively reach user_input_number
                computer_guess = round((computer_min+computer_max)/2)
            
                print("My guess is:", computer_guess)
                user_input_feedback = int(input('''\nAm I?\n1. Too low.\n2. Correct.\n3. Too high.\n\nWhich one (1 to 3): '''))
                
                if user_input_feedback == 3:
                    computer_max = computer_guess
                    
                elif user_input_feedback == 1:
                    computer_min = computer_guess
                    
                elif user_input_feedback == 2:
                    user_repeat_input = input("I'm the best bot! Easy. Want to see my magic again (y or n)?: ")
                    
                    if user_repeat_input == "y":
                        repeat_stat = 2
                        break
                    else:
                        repeat_stat = 1
                    break
main()