"""
Author: Darrien Guan
Date: Oct 24
Discription: Expand date function.
"""

def expand_date(input_date):
    '''Converts mm/dd/yyyy to regular form: eg. September, 12, 2023'''

    # Corresponding number and word.
    month_dictionary = [(1, "January"),(2, "Febuary"),(3, "March"),(4, "April"),(5, "May"),(6, "June"),(7, "July"),(8, "August"),(9, "September"),(10, "October"),(11, "November"),(12, "December")]

    # Split input date into list, then convert numerical month to word.
    list_date = input_date.split("/")
    month = month_dictionary[int(list_date[0])-1][1]
    
    # Return month in word format along with date and year
    return f"{month}, {list_date[1]}, {list_date[2]}"

def main():
    '''main logic'''

    # Asks user for input
    input_date = input("Enter a date in mm/dd/yyyy format: ")

    # Output results
    print("The date is:", expand_date(input_date))