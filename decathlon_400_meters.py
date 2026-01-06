#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 20:43:50 2025

@author: rupertjwebb
"""
import random

class Die:
    '''Die class'''

    def __init__(self, sides=6):
        '''Die(sides)
        creates a new Die object
        int sides is the number of sides
        (default is 6)
        -or- sides is a list/tuple of sides'''
        # if an integer, create a die with sides
        #  from 1 to sides
        if isinstance(sides, int):
            self.numSides = sides
            self.sides = list(range(1, sides + 1))
        else:  # use the list/tuple provided
            self.numSides = len(sides)
            self.sides = list(sides)
        # roll the die to get a random side on top to start
        self.roll()

    def __str__(self):
        '''str(Die) -> str
        string representation of Die'''
        return 'A ' + str(self.numSides) + '-sided die with ' + \
               str(self.get_top()) + ' on top'

    def roll(self):
        '''Die.roll()
        rolls the die'''
        # pick a random side and put it on top
        self.top = random.choice(self.sides)

    def get_top(self):
        '''Die.get_top() -> object
        returns top of Die'''
        return self.top

    def set_top(self, value):
        '''Die.set_top(value)
        sets the top of the Die to value
        Does nothing if value is illegal'''
        if value in self.sides:
            self.top = value

def decathlon_400_meters():
    '''decathlon_400_meters() -> int
    plays a solitare version of Reiner Knizia's 400 Meters
    returns final score'''
    # initializes rerolls, score, and dice
    score = 0
    rerolls = 5
    die1 = Die([1, 2, 3, 4, 5, -6])
    die2 = Die([1, 2, 3, 4, 5, -6])

    # play 4 rounds
    for gameRound in range(1, 5):
        print("Your total score so far is " + str(score))
        print("Round " + str(gameRound) + " -- you have " + \
              str(rerolls) + " rerolls left.")
        while True:
            # roll the dice
            input("Press enter to roll.")
            die1.roll()
            die2.roll()
            roundScore = die1.get_top() + die2.get_top()
            print("You rolled " + str(die1.get_top()) + " and " + \
                  str(die2.get_top()) + " for a total of " + str(roundScore))

            # if the player has no rerolls, they're stuck with this
            if rerolls == 0:
                print("You're out of rerolls, so you have to keep this.")
                break

            # see if they want to reroll
            response = 'x'  # setting the value to 'x' ensures we enter the while loop
            while response.lower() not in ['y', 'n']:
                response = input("Do you want to reroll (y/n)? ")

            if response.lower() == 'n':
                break  # keeping this roll, move on the the next roll

            # they're using a reroll
            rerolls -= 1
            print("OK, you have " + str(rerolls) + " rerolls left.")

        score += roundScore  # update the score

    return score

score = decathlon_400_meters()
print("Your final score is: " + str(score))