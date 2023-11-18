"""
Author: Darrien Guan
Date: November 18, 2023
Discription: Modification to the teacher class
"""

class Teacher:
    def __init__(self):
        self.__name = "Ms. Huynh"
        self.__mood = "content"

    def catch_late_student(self):
        self.__mood = "unhappy!"

    def mark_good_test(self):
        self.__mood = "delighted!"

    def get_name(self):
        return self.__name
    
    def get_mood(self):
        return self.__mood
    
    def __str__(self):
        "This method returns a string indicating the object's state."
        return self.__name + " is " + self.__mood