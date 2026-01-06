#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 12:26:19 2024

@author: webbkids
"""
def count_letter(string,letter):
    '''count_letter(string,letter) -> str
    returns string with all occurrences of letter counted'''
    endString = 0
    for i in string:
        if  i == letter:
            endString += 1
    
    return endString
#print(count_letter("stringg", "g"))

def most_common_letter(string):
    '''most_common_letter(string) -> str
    returns the lowercase letter that's most common in string'''
    letters = 'abcdefghijklmnopqrstuvwxyz'
    mostLetter =''
    mostLetterNum = 0
    letterNum = 0
    for letter in letters:
        letterNum = count_letter(string, letter)
        if letterNum > mostLetterNum:
            mostLetter = letter
            mostLetterNum = letterNum
        
        letterNum = 0
        
    return mostLetter
        
# example
excerpt = '''
"My dear fellow," said Sherlock Holmes as we sat on either side of the fire in his lodgings at 
Baker Street, "life is infinitely stranger than anything which the mind of man could invent. We 
would not dare to conceive the things which are really mere commonplaces of existence."
'''
# by Sir Arthur Conan Doyle
print(most_common_letter(excerpt))