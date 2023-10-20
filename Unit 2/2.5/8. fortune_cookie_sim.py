"""
Author: Darrien Guan
Date: September 29, 2023
Description: Simulates fortune cookie messages.
Note: I had to use features I don't think we learned but I couldn't find another way to meet the requirements.
"""
import random

# GLOBAL CONSTANTS
NUMBER_OF_FORTUNES = 5

# Global variables
fortune_messages = ["You are truely inspirational.", "Your future is brighter than the sun.", "I like your shoes, they're nice.", "I'm some random office worker that writes fortunes for you.", "I told ya, fortune cookies are worth cracking open!", "You are now reading a true master's work.", "This is a true work of art"]

def random_fortunes():
    '''Function prints 5 random unique fortunes from fortune_messages list'''
    
    # Generates a random number from 1 to 5.
    random_index = random.shuffle(fortune_messages)
    
    for i in range(NUMBER_OF_FORTUNES):
        print("Your fortune:", fortune_messages[i])
    
def main():
    '''mainline logic'''
    
    # Calls random fortunes function.
    random_fortunes()
    
main()