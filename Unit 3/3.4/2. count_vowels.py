"""
Author: Darrien Guan
Date: Oct 19
Discription: counts number of vowels in a string
"""

def count_vowels(input_string):
    '''count number of vowels'''
    
    # Counter for each vowel letter.
    a_count = 0
    e_count = 0
    i_count = 0
    o_count = 0
    u_count = 0
    
    # Checks each character in string for vowel.
    for i in range(len(input_string)):
        character = input_string[i].lower()
        
        # If vowel is present, count is increased by 1
        if character == "a":
            a_count += 1
        elif character == "e":
            e_count += 1
        elif character == "i":
            i_count += 1
        elif character == "o":
            o_count += 1
        elif character == "u":
            u_count += 1
        
    return a_count, e_count, i_count, o_count, u_count
        
def main():
    '''mainlogic'''
    
    # Ask user for input
    input_string = input("Enter a string to count vowels: ")
    
    # Call count_vowels function with user input.
    number_of_vowels = count_vowels(input_string)
    
    # Display results.
    print("""Number of a: %i
Number of e: %i
Number of i: %i
Number of o: %i
Number of u: %i""" % (number_of_vowels[0], number_of_vowels[1], number_of_vowels[2], number_of_vowels[3], number_of_vowels[4]))
    
main()