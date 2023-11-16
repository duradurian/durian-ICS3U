"""
Author: Darrien Guan
Date: November 15, 2023
Discription: Teacher class that with 4 methods.

Question answer: Since only functions within the class can change the name or 
mood attributes within the class, there is no way to change these attributes
outside of the class using ANY outside code, including main line logic code.

What you CAN do: You can create a function within the class to change the
mood or name attribute. Since you can already change the mood attribute,
below is a demo of new code of showing how to change name attribute.
"""

class Teacher:
    def __init__(self):
        self.name = "Ms. Huynh"
        self.mood = "content"

    def catch_late_student(self):
        self.mood = "unhappy!"

    def mark_good_test(self):
        self.mood = "delighted!"

    def get_name(self):
        return self.name
    
    def get_mood(self):
        return self.mood
    
    # Function that changes name attributes
    def change_name(self, new_name):
        self.name = new_name
    
def main():

    instructor = Teacher()

    # Original name.
    print("The instructor is", instructor.get_name())

    # Ask user for input and use change_name method.
    new_name = input("Enter a new instructor: ")
    instructor.change_name(new_name)

    # Display name change.
    print("The new instructor is", instructor.get_name())
    

main()