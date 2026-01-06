#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 12:00:50 2024

@author: webbkids
"""

def translate():
    '''translate() -> None
    Prompts user to enter dictionary files and input and output files
    Changes words in input file according to the dictionary file
    Write translation in output file'''
    dictFileName = input('Enter name of dictionary: ')
    textFileName = input('Enter name of text file to translate: ')
    outputFileName = input('Enter name of output file: ' )
    # add your code here