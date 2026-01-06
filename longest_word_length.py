#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 19:36:02 2024

@author: webbkids
"""

def longest_word_length(string):
    wordlist =  string.split()
    longestLenth = 0
    for word in wordlist:
        if len(word) > longestLenth:
            longestLenth = len(word)
    return longestLenth

def longest_word_lengths(string):
    '''longest_word_length(string) -> str
    returns the length of the longest word in string'''
    wordList = string.split()
    lengthList = []  # creates an empty list
    for word in wordList:
        lengthList.append(len(word))
    return max(lengthList)

def longest_word_length_2(string):
    '''longest_word_length_2(string) -> str
    returns the length of the longest word in string'''
    longest_word = max(string.split(), key=len)  # finds the longest word in string
    return len(longest_word)  # returns the length of the longest word


print(longest_word_length_2("art of problem solving"))