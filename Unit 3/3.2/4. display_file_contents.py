"""
Author: Darrien Guan
Date: October 11, 2023
Discription: Program handles exceptions caused by divide by zero errors.
"""

def main():
    '''main logic'''

    # loops until a file is successfully printed.
    while True:
        try:
            # Asks user for input.
            file_name = input("Enter the file name to display: ")

            # Attempts to read and display file.
            contents = open(file_name, "r")
            print(contents.read())
            break

        except FileNotFoundError:
            # If cannot read, displays message and user can try again.
            print("Error has occured, file not found.")
main()