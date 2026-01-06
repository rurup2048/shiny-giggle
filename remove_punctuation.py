#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 20:17:32 2024

@author: webbkids
"""

def remove_punctuation(s):
    sWithoutPunct = ""
    for letter in s:
        if letter not in punctuation:
            sWithoutPunct += letter
    return sWithoutPunct