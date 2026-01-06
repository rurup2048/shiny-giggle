#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 18:50:25 2024

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