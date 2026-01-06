#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 19:58:58 2024

@author: webbkids
"""

# multiplication table for digits
# print the top row
topRowString = ''            # will contain top row
for column in range(10):     # column goes from 0 to 9
    topRowString += '\t' + str(column) # add tab and column label
print(topRowString)          # print top row
for i in range(10):
    print("-", end= '\t')
print("")

for row in range(10):        # row goes from 0 to 9
    rowString = str(row)     # row label
    for column in range(10): # column goes from 0 to 9
        rowString += '\t' + str(row * column) # add tab and product
    print(rowString)         # print row