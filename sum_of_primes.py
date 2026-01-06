#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 12:54:07 2024

@author: webbkids
"""

def is_multiple(x, y):
    '''is_multiple(x, y) -> bool
    returns True if x is a multiple of y, False otherwise
    x, y: int
    '''
    #print("Checking if " + str(x) + " is a multiple of " + str(y))  # TEST PRINT
    # check if y divides evenly into x
    return (x % y == 0)

def is_prime(n):
    '''is_prime(n) -> bool
    returns True if n is prime, False if n is not prime
    n: int
    '''
    isPrime = True  # initialize the isPrime variable

    # check every divisor from 2 up to sqrt(n)
    for div in range(2, int(n**0.5) + 1):
        #print("div = " + str(div))  # TEST PRINT
        if is_multiple(n, div):
            isPrime = False  # n isn't prime!

    return isPrime

def sum_of_primes(k):
    '''sum_of_primes(k) -> int
    returns sum of the first k primes'''
    total = 0  # running total
    nextNumber = 2 
    for i in range(k):
        while not is_prime(nextNumber): # find the next prime
            nextNumber += 1
        total += nextNumber  # we found a prime, add it to the total
        nextNumber += 1  
    return total

num = int(input("how long -> "))
for i in range(num):
   if is_prime(i):
      print(i)
    