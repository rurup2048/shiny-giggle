#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 17:07:59 2024

@author: webbkids
"""

def make_acronym(string):
    acronym = ""
    sentence = string.split()
    for word in sentence:
        acronym += word[0]
    
    return acronym

print(make_acronym('Art of Problem Solving'))
# print('Art of Problem Solving'.split())