#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 18:09:31 2025

@author: rupertjwebb
"""

from tkinter import *

class Clicks(Frame):
    '''creates a hello world window'''

    def __init__(self, master):
        '''HelloWorldFrame()
        creates a new HelloWorldFrame'''
        self.numClicks = 0
        Frame.__init__(self, master)  # set up as a Tk frame
        self.grid()  # place the frame in the root window
        # create a button
        self.hwButton = Button(self, text='Click me!', command=self.print_message)
        self.hwButton.grid(row=0, column=0)
        # create a text display
        self.hwMessageBox = Label(self, text="I'm waiting...")
        self.hwMessageBox.grid(row=1, column=0)

    def print_message(self):
        '''prints hello world message'''
        self.numClicks += 1
        self.hwMessageBox['text'] = 'you have clicked the button' +str(self.numClicks)+' times'

root = Tk()
hwf = Clicks(root)
hwf.mainloop()