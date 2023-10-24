"""
Author: Darrien Guan
Date: Oct 24
Discription: Methods of adding name to end of list.
"""

def main():
    '''main logic'''

    names = []

    # Add dog element first using append.
    names.append("dog")

    # Add cat to end of existing list using insert.
    names.insert(len(names), "cat")

    # Add bear using concatenation.
    names = names + ["bear"]

    # Display end result.
    print(names)

main()