#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 14:17:07 2025

@author: webbkids
"""

def prime_factorization(num, wantDict=False):
    ''' prime_factorization(int, bool) -> str
    returns the prime factorization in a str'''
    primes = {}  # keep track of the primes
    divisor = 2  # keep track of the divisor

    while num > 1:
        divisorCount = 0  # keeps track of how many times
                          # we can divide divisor into num
        while num % divisor == 0:  # divisor is a factor
            num = num // divisor
            divisorCount += 1

        if divisorCount > 0:   # if we had any, add a dict entry
            primes[divisor] = divisorCount

        divisor += 1  # increment the divisor

    # testing -- just return the dict
    if wantDict:
        return primes
    else:
        primeList = list(primes.keys())
        primeList.sort()
        output = ''
        
        for prime in primeList:
            output += str(prime) 
            if primes[prime] > 1:  # need to add an exponent
                output += '^' + str(primes[prime])
            output += ' * ' # add multiplication symbol

    return output[:-3]

while True:
    sun = input('-> ')
    print(prime_factorization(int(sun)))
        