#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 21:00:20 2024

@author: webbkids
"""
def is_jolly(inList):
    """is_jolly(inList) -> boolean
    Returns True if inList is a jolly jumper sequence and False
    otherwise."""
    if len(inList) < 3:
        return True
    diff = abs(inList[0] - inList[1])
    for i in range(len(inList) - 2):
        diff = diff - 1
        if not abs(inList[i + 1] - inList[i + 2]) == diff:
            #print (str(diff) + ":" + str(i) + ":" + str(inList[i + 2]) + "-" + str(inList[i + 3]))
            return False
    return True

# test cases
print(is_jolly([6,9,7,8]))  # should be True
print(is_jolly([1,4,3,2]))  # should be False