"""
Author: Darrien Guan
Date: September 29, 2023
Description: Basic, no logic, rock paper scissors bot.
"""

import random

def rps_generator():
    '''Randomly selects rock (1) paper (2) or scissors (3).'''
    
    # returns random value from 1 to 3.
    return random.randint(1,3)
    
def rps_winner_calculation(computer, user):
    '''Efficient algorithm that took me too long: Given computer and user input, function outputs the winner.'''
    
    if computer == user:
        return "draw"
    
    elif (computer + 1) % 3 == user:
        return "user"
    
    else: return "computer"
    
def num_to_rps(rps_number):
    '''converts number to rock, paper, or scissor string.'''
    
    # Returns rock, paper, or scissor based on numbers 1 to 3.
    if rps_number == 1:
        return 'rock'
    elif rps_number == 2:
        return 'paper'
    elif rps_number == 3:
        return 'scissors'
    else: return None
        
def main():
    '''mainline logic'''
    
    # Nested while loop
    while True:
        
        # Input validation for rock, paper, scissor input (1 to 3)
        while True:
            user_rps_input = int(input("rock (1), paper (2), or scissors (3)? Please type in number: "))
            
            if user_rps_input >= 1 and user_rps_input <= 3:
                break
            
            else: print("Invalid response, please enter a valid number.")
        
        # Generates random value from 1 to 3 (corresponds with rock, paper or scissors.)
        computer_rps_value = rps_generator()
        
        # Displays who won and repeats loop if it is a draw or there is an error.
        if rps_winner_calculation(computer_rps_value, user_rps_input) == "draw":
            print("It was a draw, both you and the computer selected", num_to_rps(computer_rps_value))
            
        elif rps_winner_calculation(computer_rps_value, user_rps_input) == "computer":
            print("The computer won, it drew " + num_to_rps(computer_rps_value))
            break
            
        elif rps_winner_calculation(computer_rps_value, user_rps_input) == "user":
            print("Congrats, you won the game. The computer drew " + num_to_rps(computer_rps_value))
            break
            
        else: 
            print("Error, trying game again...")
            
main()