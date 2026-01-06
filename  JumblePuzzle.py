#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  6 14:50:59 2025

@author: webbkids
"""
def listToStr(List):
    endstr = ''
    for char in List:
        endstr += char
    return endstr

def permute(inputList):
    '''permute(inputList) -> list
    returns list of all permutations of inputList'''
    if len(inputList) == 0:
        return [[]]
    
    permutations = []
    for i in range(len(inputList)):
        firstElement = inputList[i]
        restElements = inputList[:i] + inputList[i+1:]
        
        miniPermutations = permute(restElements)# the recursive part
        
        for miniPermutation in miniPermutations:
            permutations.append([firstElement] + miniPermutation)
            
    return permutations

def Jumble_Puzzle(word):
    ''' Jumble_Puzzle(str word) -> str
    word puzzles that involve unscrambling jumbled 
    words to solve a clue'''
    infile = open('wordlist.txt','r')
    words = list(infile.readlines())
    infile.close()
    for scramled in permute(list(word.lower())):
        #print(permute(list(word.lower())))
        #print(listToStr(scramled)+'\n')
        if listToStr(scramled)+'\n' in words:
            return listToStr(scramled)

print(Jumble_Puzzle('CHWAT')) # watch
print(Jumble_Puzzle('RAROM')) # armor
print(Jumble_Puzzle('CEPLIN')) # pencil
print(Jumble_Puzzle('YAFLIM')) # family
        
        