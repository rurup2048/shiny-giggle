#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 16:49:01 2024

@author: webbkids
"""

inFile = open("wordlist.txt","r")
words = inFile.readlines()
inFile.close()

outFile = open("8_letter_wordlist.txt", "w")
i = 0
for word in words:
    word = word.strip()
    if len(word) == 8:
        outFile.write(word)
        i += 1
print(i)
outFile.close()