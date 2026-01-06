#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 20:36:43 2024

@author: webbkids
"""
def is_multiple(x, y):
    '''is_multiple(x, y) -> bool
    returns True if x is a multiple of y, False otherwise
    x, y: int
    '''
    print("Checking if " + str(x) + " is a multiple of " + str(y))  # TEST PRINT
    # check if y divides evenly into x
    return (x % y == 0)

def is_prime (n):
    '''is_prime(n) -> bool
    returns True if n is prime, False if n is not prime
    n: int
    '''
    isPrime = True  # initialize the isPrime variable

    # check every divisor from 2 up to sqrt(n)
    for div in range(2, int(n**0.5) + 1):
        print("div = " + str(div))  # TEST PRINT
        if is_multiple(n, div):
            isPrime = False  # n isn't prime!

    return isPrime

print(is_prime(11))