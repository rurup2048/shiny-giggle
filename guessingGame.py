#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 14:08:50 2024

@author: webbkids
"""

import random

numGuesses = 0
targetNum = random.randint(0, 100)

while True:
    guess = int(input("guess a number from 0-100 ->  "))
    
    if targetNum < guess:
        print("guess a lower number than " + str(guess))
        numGuesses += 1
    elif targetNum > guess:
        print("guess a higher number than " + str(guess))
        numGuesses += 1
    else:
        numGuesses += 1
        print("yay you win, you got the number " + str(targetNum))
        if numGuesses == 1:
            print("you did it, you won in " + str(numGuesses) + " guess")
        else:
            print("you did it, you won in " + str(numGuesses) + " guesses")
        break