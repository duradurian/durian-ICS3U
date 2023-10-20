"""
Author: Darrien Guan
Date: Oct 19
Discription: Scrambles letters in a word.
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
    '''mainline logic'''

    input_word = input("Enter a string to shuffle: ")
    print("Your shuffled string is:", word_jumble(input_word))

main()