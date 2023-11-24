"""
Author: Darrien Guan
Date: November 24, 2023
Discription: Displays random welcome message in a window.
"""

import tkinter
import random

class MainGUI:
    '''Main GUI class'''

    def __init__(self, welcome_message: str):
        '''initlizes variables'''
        
        self.main_window = tkinter.Tk()
        self.label = tkinter.Label(self.main_window, text = welcome_message)
        self.label.pack()
        tkinter.mainloop()

def main():
    '''main logic'''
    messages = ["Welcome to my window.", "Welcome, I love Windows.", "Bonjour, j'aime Windows.", "Wassup homie"]
    main_gui = MainGUI(random.choice(messages))

main()