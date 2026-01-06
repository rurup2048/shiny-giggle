#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 21:00:16 2024

@author: webbkids
"""
import random

def roll_die():
    return random.randint(1, 6)
    
for i in range(10):
    print(roll_die())