#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 19:16:59 2024

@author: webbkids
"""

def remove_letter(string,letter):
    '''remove_letter(string,letter) -> str
    returns string with all occurrences of letter removed'''
    endString =''
    for i in string:
        if not i == letter:
            endString += i
    
    return endString
        

# test cases
print(remove_letter('This is a test','t'))  # should print 'This is a es'
print(remove_letter('Hello World!','l'))    # should print 'Heo Word!'
print(remove_letter('I like Python','q'))   # should print 'I like Python'