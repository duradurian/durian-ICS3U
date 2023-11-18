"""
Author: Darrien Guan
Date: November 18, 2023
Discription: Class named Book that has 7 methods.
"""

class Book:
    '''Class book, with methods that set value of publisher,
    author, and title, and methods that return title, author,
    and publisher. Str method displays all three 
    instance variables.'''
    
    def __init__(self, __author, __publisher, __title):
        self.__author = __author
        self.__publisher = __publisher
        self.__title = __title
        
    def get_author(self):
        return self.__author
    
    def get_publisher(self):
        return self.__publisher
    
    def get_title(self):
        return self.__title
    
    def change_publisher(self, publisher):
        self.__author = publisher
        
    def change_author(self, author):
        self.__publisher = author
        
    def change_title(self, title):
        self.__title = title
        
    def __str__(self):
        return f"Author: {self.__author}, Publisher: {self.__publisher}, Title: {self.__title}"
    
def main():
    '''main logic'''
    
    # New object instance
    new_book = Book("Yes", "Pub", "Best Book")
    
    # Displays original obj
    print(new_book)
    
    # Set values using methods
    new_book.change_author("Darrien")
    new_book.change_publisher("Darrien PUB")
    new_book.change_title("Darrien's Book")
    
    # Display __str__() method.
    print(new_book)
    
    # Alternate way to display using desinged methods
    print(f"Author: {new_book.get_author()}, Publisher: {new_book.get_publisher()}, Title: {new_book.get_title()}")
    
main()