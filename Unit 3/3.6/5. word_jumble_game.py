"""
Author: Darrien Guan
Date: Oct 24
Discription: Program chooses random word and user guesses word using letters.
"""

import random

def word_jumble(input_word):
    '''Shuffles letters in the word.'''

    word = input_word
    new_word = ""
    length = len(input_word)

    # keeps repeating as long as there are still characters in word
    while len(word) > 0:
        index_random = random.randint(0, len(word) - 1)
        new_word = new_word + word[index_random]
        word = word[:index_random] + word[index_random + 1:]

    return new_word

def main():
    '''main logic'''

    word_list= ["whooper", "nuggets", "chicken"]

    # Keeps repeating until there are no words remaining in words list.
    while True:

        if len(word_list) <= 0:
            break
        
        # Select random word from words list
        random_word = random.choice(word_list)

        # Jumble the word using the word_jumble func
        word_jumbled = word_jumble(random_word)

        # Ask user for input.
        user_guess = input(f"The jumbled word is {word_jumbled}, what is the word?: ")

        # If the user guess and random word is the same, remove the word from the list.
        if user_guess == random_word:
            print("Correct word! Epic, awesome!")
            word_list.remove(random_word)

    print("Congrats, you've guessed all the words!")

    if input("Press any key to exit: "):
        exit()

main()