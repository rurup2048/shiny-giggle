#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 11:36:08 2024

@author: webbkids
"""

import random

def roll_die():
    return random.randint(1, 6)

def backgammon_roll():
    dice1 = roll_die()
    dice2 = roll_die()
    if dice1 == dice2:
        return (dice1 + dice2) * 2
    else:
        return dice1 + dice2
    
p1num = 0    
p2num = 0    

while True:
    input("player 1 press enter to roll")
    p1roll = backgammon_roll()
    p1num += p1roll
    print("player 1 rolled and got  " + str(p1roll) + " and there total is " + str(p1num))
    print("\n")
    
    input("player 2 press enter to roll")
    p2roll = backgammon_roll()
    p2num += p2roll
    print("player 2 rolled and got  " + str(p2roll) + " and there total is " + str(p2num))
    print("\n")
    
    input("lets see who is wining (press enter to see who is wining)")
    
    if p1num > p2num:
       print("player 1 wining by " + str(p1num - p2num))
       print("\n")
    elif p1num < p2num:
       print("player 2 wining by " + str(p2num - p1num))
       print("\n")
    else:
       print("It's a tie")
       print("\n")
    
    if p1num >= 100 or p2num >= 100:
        break

if p1num > p2num:
   print("player 1 wins by " + str(p1num - p2num))
elif p1num < p2num:
   print("player 2 wins by " + str(p2num - p1num))
else:
   print("It's a tie")