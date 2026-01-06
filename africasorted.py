#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 20:54:14 2024

@author: webbkids
"""
def somthing(file):
    inFile = open(file, 'r')         # open africa.txt for reading in
    countries = inFile.readlines()           # read all lines into a list
    inFile.close()                           # close the file
    countries.sort()                         # sort in alphabetical order
    
    longestLength = 0  # initialize longest length
    for country in countries:
        if len(country) > longestLength:  # found new longest length
            longestLength = len(country)  # save the new longest length
    
    outFile = open('africasorted.txt', 'w')  # open the output file
    for country in countries:
        outputLine = country
        outputLine.strip('\n')
        outputLine += ' '*(longestLength-len(country))  # padding
        outputLine += ' '  # space between name and digit(s)
        if len(country) < 10:
            outputLine += ' '   # extra space for single-digit numbers
        outputLine += str(len(country))
        outFile.write(outputLine)
    outFile.close()
somthing('africa.txt')