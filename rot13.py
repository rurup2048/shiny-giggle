#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 15:37:51 2024

@author: webbkids
"""

def rot13(inputStr):
    endString = ''
    abcs = "'abcdefghijklmnopqrstuvwxyz'"
    for letter in inputStr:
        if letter in abcs or letter in abcs.upper():
            end = ord(letter) + 13
            if (letter.islower() and end >= 123) or (letter.isupper() and end >= 91):
                end += -26
        else:
            end = ord(letter)
        endString += chr(end)
        
    return endString

print(rot13('Hello, World!'))