#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 21:36:11 2024

@author: webbkids
"""

# open the files
inFile = open("classgrades.txt", 'r')    # open in-file
outFile = open('classscores.txt','w')    # open out-file
lines = inFile.readlines()               # read in-file
inFile.close()                           # close in-file
for line in lines:                       # setup loop
    line.strip()                         # get rid of the \n
    gradeLines = line.split()            # gets the line 
    numGrades = len(gradeLines) -1       # get the number of grades
    Sum = 0                              # the future sum of grades
    for i in range(1,numGrades+1):       # add grade to Sum
        Sum += int(gradeLines[i]) 
    outFile.write(gradeLines[0] +' got ' + str(round(Sum/numGrades)) +'\n') # print the grade
outFile.close()                          # close out-file
print('the grades have been graded.')    # done
        
        