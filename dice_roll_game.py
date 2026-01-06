#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 19:31:57 2024

@author: webbkids
"""

def roll_die(): #this rolls the die
    return random.randint(1, 6)

import random

# setup
size = int(input("how big do you want your chart to be -> "))
print("Roll    Number")
print("----    ------")
for i in range(2,size + 1): 
    roll = 0
    for rolls in range(i * 2): # this tells how many times does the dice roll
        roll += roll_die() # this rolls the dice
    lens = 8 - len(str(i)) # this gets the spacing right
    print(str(i) + (' ' * lens) + str(roll)) # this prints the whole thing out
