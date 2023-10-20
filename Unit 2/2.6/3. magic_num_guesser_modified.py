"""
Author: Darrien Guan
Date: September 29, 2023
Description: Users guess a randomly selected number between 1 and 1000 with feedback from the bot on every guess. 10 Attempts max.
"""

import random

# GLOBAL CONSTANTS
NUMBER_OF_ATTEMPTS = 10

def user_result_output(computer_selection, user_selection):
    '''Returns the corresponding number which represents whether the computer selection is greater or less than the user selection or if they're equal.'''
    
    # Returns corresponding number result.
    if computer_selection > user_selection:
        return 1
    
    elif computer_selection < user_selection:
        return 2
    
    elif computer_selection == user_selection:
        return 3

def main():
    '''mainline logic'''
    
    # Whether the while loop should repeat or not.
    repeat_status = 0
    
    # Nested while loops
    while True:
        
        # Stops loop if repeat_status is 1.
        if repeat_status == 1:
            break
        
        # Generates random number between 1 and 1000
        computer_selection = random.randint(1,1000)
        
        attempts_remaining = NUMBER_OF_ATTEMPTS-1
        
        while True:
            user_selection = int(input("Enter a number between 1 and 1000: "))
            
            user_feedback = user_result_output(computer_selection, user_selection)
            
            # Display whether user input is too high or too low, if if its the same as computer selection or if no more attepmts remaining.
            if attempts_remaining == 0:
                user_game_input1 = input("You have ran out of attempts; the number was " + str(computer_selection) + ". Would you like to play again (y or n)?: ")
                
                # Sets repeat status to either 0 or 1, which determines whether the while loop will repeat.
                if user_game_input1 == "y":
                    repeat_status = 0
                    break
                
                elif user_game_input1 == "n": 
                    repeat_status = 1
                    break
        
            elif user_feedback == 1:
                print("Too low. Try again! " + str(attempts_remaining) + " remaining.")
                attempts_remaining -= 1
                
            elif user_feedback == 2:
                print("Too high. Try again! " + str(attempts_remaining) + " remaining.")
                attempts_remaining -= 1
                
            elif user_feedback == 3:
                
                user_game_input2 = input("Excellent! You guessed the number! Would you like to play again (y or n)?: ")
                
                # Sets repeat status to either 0 or 1, which determines whether the while loop will repeat.
                if user_game_input2 == "y":
                    repeat_status = 0
                    break
                
                elif user_game_input2 == "n": 
                    repeat_status = 1
                    break
                
            else: print("Error. try again!")
    
main()