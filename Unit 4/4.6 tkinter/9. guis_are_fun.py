"""
Author: Darrien Guan
Date: November 24, 2023
Discription: Displays GUIs are fun message in window.
"""

import tkinter

class MainGUI:
    '''Main GUI class'''

    def __init__(self):
        '''initlizes variables'''
        
        self.main_window = tkinter.Tk()
        self.label = tkinter.Label(self.main_window, text = "GUIs are fun!")
        self.label.pack()
        tkinter.mainloop()

def main():
    '''main logic'''

    main_gui = MainGUI()

main()