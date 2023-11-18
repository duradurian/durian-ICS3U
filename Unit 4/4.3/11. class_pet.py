"""
Author: Darrien Guan
Date: November 18, 2023
Discription: Class named Pet which has 6 methods
"""

class Pet:
    ''' Pet class with name, animal_type, and age.
    Methods to change instance variables and return instance
    variables.'''
    
    def __init__(self, __name, __animal_type, __age):
        self.__name = __name
        self.__animal_type = __animal_type
        self.__age = __age
        
    def set_name(self, name):
        self.__name = name
        
    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type
        
    def set_age(self, age):
        self.__age = age
        
    def get_name(self):
        return self.__name
        
    def get_type(self):
        return self.__animal_type
    
    def get_age(self):
        return self.__age
    
def main():
    '''mainlogic'''
    
    new_pet = Pet("Fluffy", "Dog", 7)
    
    # Displays pet status
    print("The pet's name is", new_pet.get_name())
    print("The pet's type is", new_pet.get_type())
    print("The pet's age is", str(new_pet.get_age()) + "\n")
    
    # Get uesr input
    new_pet.set_name(input("Enter the pet's updated name: "))
    new_pet.set_animal_type(input("Enter the pet's updated type: "))
    new_pet.set_age(input("Enter the pet's updated age: "))
    
    # Displays new pet status
    print("\nThe pet's updated name is", new_pet.get_name())
    print("The pet's updated type is", new_pet.get_type())
    print("The pet's updated age is", new_pet.get_age())
    
main()