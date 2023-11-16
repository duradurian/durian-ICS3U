"""
Author: Darrien Guan
Date: November 15, 2023
Discription: Teacher class that with 4 methods.
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
    
def main():
    huynh = Teacher()
    print (huynh.get_name(), "is", huynh.get_mood())
    print ("\nOh no, a student just came in late!")
    huynh.catch_late_student()
    # huynh.mood = "thrilled!"
    print (huynh.get_name(), "is", huynh.get_mood())
    print ("\nGreat, we just aced our test!")
    huynh.mark_good_test()
    print (huynh.get_name(), "is", huynh.get_mood())

main()