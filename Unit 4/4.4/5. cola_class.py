"""
Author: Darrien Guan
Date: November 21, 2023
Discription: Cola subclass
"""

class Beverage:
    def __init__(self, bev_name):
        self.__bev_name = bev_name

class Cola(Beverage):
    def __init__(self):
        '''__init__() calls beverage's __init__ function'''
        Beverage.__init__(self, "cola")