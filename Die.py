#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 20:12:54 2025

@author: rupertjwebb
"""

import random

class Die:
    '''Die class'''

    def __init__(self, sidesParam=6):
        '''Die([sidesParam])
        creates a new Die object
        int sidesParam is the number of sides
        (default is 6)
        -or- sidesParam is a list/tuple of sides'''
        # if an integer, create a die with sides
        #  from 1 to sides
        if isinstance(sidesParam, int):
            sidesParam = range(1, sidesParam + 1)
        self.sides = list(sidesParam)
        self.numSides = len(self.sides)
        # roll the die to get a random side on top to start
        self.roll()

    def __str__(self):
        '''str(Die) -> str
        string representation of Die'''
        return 'A ' + str(self.numSides) + '-sided die with ' + \
               str(self.get_top()) + ' on top'

    def roll(self):
        '''Die.roll()
        rolls the die'''
        # pick a random side and put it on top
        self.top = random.choice(self.sides)

    def get_top(self):
        '''Die.get_top() -> object
        returns top of Die'''
        return self.top

    def set_top(self, value):
        '''Die.set_top(value)
        sets the top of the Die to value
        Does nothing if value is illegal'''
        if value in self.sides:
            self.top = value
        
    def flip(self):
        ''' die.flip() -> str or int
        flips self.top'''
        return self.numSides - self.sides.index(self.get_top())
        
        
        

d = Die(8)
print(d)
d.set_top(3)
print(d)
d.flip()
print(d)