#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 13:57:09 2024

@author: webbkids
"""
def checkGrade(grade):
    if grade >= 96:
        print("yay, you got an A+")
    elif grade >= 88:
        print("way to go, you got an A")
    elif grade >= 85:
        print("keep going, you got an B+")
    elif grade >= 80:
        print("keep going, you got an B")
    elif grade >= 77:
        print("keep going, you got an C+")
    elif grade >= 70:
        print("keep going, you got an C")
    elif grade >= 66:
        print("keep going, you got an D+")
    elif grade >= 50:
        print("keep trying, you got an F")
    else:
        print("keep going, you got an I")
        
checkGrade(55)