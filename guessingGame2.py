#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 15:10:17 2025

@author: webbkids
"""

import random
import time

def textRoll(text): # this code repleases print(), this was for fun :-)
    for letter in text:
        print(letter, end='', flush=True)
        time.sleep(.07)

playerGuess = 0
numToGuess = random.randint(1, 100)
numGuesses = 0

textRoll('im thinking of a number from 1 to 100, guess my number.\n')
while not numToGuess == playerGuess: 
    playerGuess = 0
    numGuesses += 1
    
    while not playerGuess in range(1, 100): # this code is the input
        textRoll('guess a number -> ')
        playerGuess = int(input())
    
    if not numToGuess == playerGuess: # this code checks to see if you were over or under the target number
        if playerGuess > numToGuess:
            textRoll('your guess is too high, ')
        else:
            textRoll('your guess is too low, ')

if numGuesses == 1:
    textRoll(f'\nyou won in {numGuesses} guess (wow, you are good at guessing games) \nGAME OVER')
else:
    textRoll(f'\nyou won in {numGuesses} guesses \nGAME OVER')
