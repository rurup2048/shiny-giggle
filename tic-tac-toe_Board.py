#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 17:22:18 2024

@author: webbkids
"""
def print_board(tttList):
    '''print_board(tttList) -> None
    prints a tic-tac-toe_Board corresponding to tttList'''
    row = 0
    for i in tttList:
        row += 1
        if row % 3 == 1 and row != 1:# checks to see if to end the row
            print("-+-+-")
        if row % 3 == 0 and row != 1:# this checks to see if ineed a "|"
            print(i, end= "\n")
        else:
            print(i, end= "|")

print_board(['O', 'O', 'X','O', 'X', 'X','X', 'O', 'O'])

'''
should print:
 |O|X
-+-+-
 |X|X
-+-+-
 |O|O
'''
