#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 17:35:15 2024

@author: webbkids
"""
def the_Fibonacci_sequence(size):      # find this many Fibonacci numbers
    fib = [0,1]        # start with an empty list # save the first two numbers
    for i in range(size - 2): # start a for loop
        fib.append(fib[-1] + fib[-2])
    return fib

print(the_Fibonacci_sequence(16))      # print the Fibonacci sequence
# if it's working correctly, it should print:
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
