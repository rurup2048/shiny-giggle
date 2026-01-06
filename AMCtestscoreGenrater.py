#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 19:22:20 2025

@author: webbkids
"""

numAnswered = int(input("Enter the number of questions answered: "))
numCorrect = int(input("Enter the number of questions correct: "))
numUnanswered = 25 - numAnswered
score = (numCorrect * 6) + (numUnanswered * 1.5) 
print("The student's score is: " + str(score))