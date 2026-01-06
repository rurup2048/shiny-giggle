#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 11:33:24 2024

@author: webbkids
"""

def changeTo_F(tempIn_C):
    newTempIn_F = 5/9 * tempIn_C - 32
    return newTempIn_F

def changeTo_C(tempIn_F):
    newTempIn_C = (tempIn_F - 32) * 5/9
    return newTempIn_C

print(changeTo_C(32))
print(changeTo_F(0))
