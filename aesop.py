#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 20:25:08 2024

@author: webbkids
"""
wordCount = {}  # empty dictionary to store the word counts
inFile = open('aesop.txt', 'r')
for line in inFile:
    line = line.lower()  # make everything lowercase
    # remove punctuation
    punctuation = '.,!?'
    for c in punctuation:
        line = line.replace(c, '')
    wordList = line.split()
    # count words
    for word in wordList:
        if word in wordCount:
            wordCount[word] += 1
        else:
            wordCount[word] = 1
inFile.close()
print(wordCount)
        
