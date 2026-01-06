#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 22:20:39 2024

@author: webbkids
"""
def multiplyGrid(fileName):
    biggestNum = 0
    infile = open(fileName, "r")
    
    for col in range(19):
        numsRows = infile.readline().split()
        for row in range(17):
            sums = int(numsRows[row]) * int(numsRows[row +1]) * int(numsRows[row +2]) * int(numsRows[row +3])
            if sums > biggestNum:
                biggestNum = sums
    
    infile = open(fileName, "r")
    numCol = infile.read().split()
    print(numCol)
    for horRows in range(17):
        for horCol in range(19):
            # sums = int(numCol[horCol + (horRows * 20)]) * int(numCol[horCol + (horRows * 20) + 20]) * int(numCol[horCol + (horRows * 20) + 40]) * int(numCol[horCol + (horRows * 20) + 60])
            sums = int(numCol[horCol + (horRows * 20)]) * int(numCol[horCol + (horRows * 20) + 20]) * int(numCol[horCol + (horRows * 20) + 40]) * int(numCol[horCol + (horRows * 20) + 60])
            print(sums)
            if sums > biggestNum:
                biggestNum = sums     
    infile.close()
    return biggestNum

print(multiplyGrid("20by20nums.txt"))