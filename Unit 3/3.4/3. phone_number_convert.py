"""
Author: Darrien Guan
Date: Oct 19
Discription: Converts alphabetical phone numbers to number.
"""

def alpha_number_convert(alpha_number):
    '''Function converts alphabetical number to number'''
    
    # Conversion dictionary
    conversion_dictionary = [(2, "abc"), (3, "def"), (4, "ghi"), (5, "jkl"), (6, "mno"), (7, "pqrs"), (8, "tuv"), (9, "wxyz")]
    new_number = ""
    
    # Checks each character in string.
    for i in range(len(alpha_number)):
        character = alpha_number[i].lower()
        
        # If the character is alphabetical, it checks for it in the conversion ditionary.
        if character.isalpha():
            
            # If chaacter present in dictionary, it adds the corresponding number to  new_number.
            for i in range(8):
                if character in conversion_dictionary[i][1]:
                    new_number += str(conversion_dictionary[i][0])
            
        else:
            new_number += alpha_number[i]
            
    return(new_number)

def number_validation(alpha_number):
    '''validates number format'''
    
    # Checks if number format is correct, else, it returns false if any requirements aren't met.
    try:
        if alpha_number[3] != "-" or alpha_number[7] != "-" or len(alpha_number) != 12:
            return False
        
        else:
            for i in range(len(alpha_number)):
                character = alpha_number[i]
                if not character.isalpha() and not character.isdigit() and character != "-":
                    return False
    
    except:
        return False
    
    # return true if false wasn't returned.
    return True

def main():
    '''mainlogic'''
    
    # Validates number before alpha_number_convert is run.
    while True:
        alpha_number = input("Enter a number to convert to regular numberical format: ")
        
        if number_validation(alpha_number):
            break
        
        else: print("Please enter a valid format (XXX-XXX-XXXX)")
    
    # Dispaly result
    print("The converted number in regular format is:", alpha_number_convert(alpha_number))
    
main()