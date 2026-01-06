#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 13:56:32 2024

@author: webbkids
"""
def is_multiple(x, y):
    if x % y == 0:
        return True
    else:
        return False

def sum_of_proper_divs(ints):
    '''6 is perfect because its proper divisors are 1, 2, and 3,
    and 1+2+3 = 6, and 28 is perfect because its proper divisors are
    1, 2, 4, 7, and 14, and 1+2+4+7+14 = 28.'''
    sums = 0
    for i in range(ints):
        if not i == 0:
            if is_multiple(ints, i):
                sums += i
    return sums == ints

for i in range(100,999):
    if sum_of_proper_divs(i):
        print(i)
