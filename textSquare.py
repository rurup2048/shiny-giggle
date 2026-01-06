#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 13:15:54 2024

@author: webbkids
"""

def letter_square (letter,size):
    square = (letter * size + "\n") * size
    return str(square)

    
print(letter_square("s", 5))