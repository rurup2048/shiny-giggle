#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 10:17:40 2024

@author: webbkids
"""

def find_winner(tttList):
    waysToWin = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
    
    stillTrue = True
    for lists in waysToWin:
        for j in lists:
            if not tttList[j] == "X":
                stillTrue = False
        if stillTrue:
            return "X wins"
        stillTrue = True
                
    stillTrue = True
    for lists in waysToWin:
        for j in lists:
            if not tttList[j] == "O":
                stillTrue = False
        if stillTrue:
            return "O wins"
        stillTrue = True
        
    return "it's a tie"
print(find_winner(['O', 'O', 'X', 'O', 'O', 'X','X', 'O', 'O']))