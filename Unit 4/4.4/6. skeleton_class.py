"""
Author: Darrien Guan
Date: November 21, 2023
Discription: Skeleton subclass 
"""

class Monster():
    def __init__(self, monster_name):
        self.set_name(monster_name)

    def set_name(self, monster_name):
        if monster_name:
            self.__name = monster_name
        else:
            self.__name = "Unknown"

    def get_name(self):
        return self.__name
    
    def speak(self):
        print ("I am a monster named " + self.__name + "." )

class Skeleton(Monster):

    def __init__(self, hungry=False):
        Monster.__init__(self, "skeleton")
        self.__hungry = hungry

    def is_hungry(self):
        return self.__hungry

    def set_hungry(self):
        self.__hungry = True