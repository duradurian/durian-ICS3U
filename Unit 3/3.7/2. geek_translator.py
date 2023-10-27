"""
Author: Darrien Guan
Date: October 26, 2023
Discription: translates geek talk to regular talk
"""

# Global dictionary
geek = {"404": "clueless. From the web error message 404, meaning page not found.",
        "Googling": "searching the Internet for background information on a person.",
        "Keyboard Plaque": "the collection of debris found in computer keyboards.",
        "Link Rot": "the process by which web page links become obsolete.",
        "Percussive Maintenance": "the act of striking an electronic device to make it work.",
        "Uninstalled": "being fired. Especially popular during the dot-bomb era."}

def look_up_term(input_term):
    '''looks up term in geek dictionary'''

    # Checks if input term is in geeks dictionary.
    if input_term in geek:
        return "The definition is: " + geek[input_term]
    
    else: return "Word not in geek dictionary."

def add_term(input_term, definition):
    '''adds a term with definitino to geek dictionary'''
    
    # Checks if input term is not in geeks dictionary, if not in, new term is added with definition.
    if input_term in geek:
        return("Word already in geek dictionary.")
    
    else:
        geek[input_term] = definition
        return "Added new term to geek dictionary."

def redef_term(input_term, new_def):
    '''redefine a term in geek dictionary'''
    
    # Checks if input term is in geeks dictionary, else, no changes are made.
    if input_term in geek:
        geek[input_term] = new_def
        return "Definition for word has been updated."

    else:
        return "Word does not previously exist in geek dictionary."

def delete_term(input_term):
    '''delete a term in geek dictionary'''

    # Checks if input term is in geeks dictionary to continue, else, no changes are made.
    if input_term in geek:
        del geek[input_term]
        return "Term has been removed from geek dictionary."
    
    else:
        return "Term does not exist in geek dictionary."

def main():
    '''main logic'''
    
    while True:
        # Ask user for input
        option_input = int(input("1 - Look Up a Geek Term \n2 - Add a Geek Term \n3 - Redefine a Geek Term \n4 - Delete a Geek Term \n5 - Quit \nEnter an option: "))
        
        # Calls corresponding funcction based on input.
        if option_input == 1:
            input_term = input("Enter the term to look up: ")
            print(look_up_term(input_term))

        elif option_input == 2:
            input_term = input("Enter the term to add: ")
            definition = input("Enter the term's definition: ")
            print(add_term(input_term, definition))

        elif option_input == 3:
            input_term = input("Enter the term to edit the definition of: ")
            new_def = input("Enter the new definition: ")
            print(redef_term(input_term, new_def))

        elif option_input == 4:
            input_term = input("Enter the term to delete: ")
            print(delete_term(input_term))

        elif option_input == 5:
            break
        
        # Tells user to press enter to continue to improve ease of use.
        input("Press enter to continue...")

main()