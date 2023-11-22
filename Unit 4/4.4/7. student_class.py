"""
Author: Darrien Guan
Date: November 21, 2023
Discription: Student subclass 
"""

class Person():
    def __init__(self, name, address, telephone):
        '''Set object variables.'''
        self.__name = name
        self.__address = address
        self.__telephone = telephone

    # Mutator methods
    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address
    
    def get_telephone(self):
        return self.__telephone
    
    # Accessor methods
    def set_name(self, new_name):
        self.__name = new_name

    def set_address(self, new_address):
        self.__address = new_address

    def set_telephone(self, new_telephone):
        self.__telephone = new_telephone

class Student(Person):

    def __init__(self, cellphone = False, student_id = 0, name = "NA", address = "NA", telephone = 0):
        '''Initalize student class as subclass of Person class.'''
        Person.__init__(self, name, address, telephone)

        # Set object variables
        self.__has_cellphone = cellphone
        self.__student_id = student_id

    # Mutator methods
    def is_cellphone(self):
        return self.__has_cellphone
    
    def get_student_id(self):
        return self.__student_id
    
    # Accessor methods
    def set_has_cellphone(self, cellphone = False):
        self.__has_cellphone = cellphone

    def set_student_id(self, student_id):
        self.__student_id = student_id

def main():
    '''main logic'''
    
    # Initialize student object instance
    student_instance = Student(True, 348592924, "Darrien", "7522 Kennedy Road", "123123123123")
    
    # Display object instance variables.
    print("Student status:")
    print("Name:", student_instance.get_name())
    print("Address:", student_instance.get_address())
    print("Student ID:", student_instance.get_student_id())
    print("Telephone:", student_instance.get_telephone())
    print("Has cellphone:", student_instance.is_cellphone())
    

main()