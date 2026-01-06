#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 13:28:24 2024

@author: webbkids
"""

def count_letters(text,letter):
    '''count_letters(text,letter) -> int
    returns number of times that letter appears in text'''
    num = 0
    for t in text:
        if t == letter.upper() or t == letter.lower():
            num += 1
    return num
        
    # you need to fill in the code here
    # to answer the question

# this gives you the answer:
quote = '''It's passed on.  
This parrot is no more.  
It has ceased to be. 
It's expired and gone to meet its maker.  
This is a late parrot.  
It's a stiff.  
Bereft of life, it rests in peace.  
If you hadn't nailed it to the perch, it would be pushing up the daisies.  
It's rung down the curtain and joined the choir invisible.  
This is an ex-parrot!'''
print(count_letters(quote,'e'))