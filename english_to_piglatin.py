#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 20:36:04 2024

@author: webbkids
"""

def english_to_piglatin(word):
    '''english_to_piglatin(word) -> string
    Translates word into Pig Latin.'''
    if word[0] in 'aeiou':  # check if the first letter is a vowel
        return word + 'way'
    # word begins with a consonant
    consonants = ''  # keep track of consonants at start of word
    while len(word) > 0 and word[0] not in 'aeiou':
        consonants += word[0]  # add the consonant
        word = word[1:]        # remove the first letter from word
    return word.lower() + consonants.lower() + 'ay'


def convert_sentence(sentence):
    '''convert_sentence(str) -> str
    Returns a Pig Latin translation of sentence.
    sentence: str
    '''
    brokenSentence = sentence.split()
    answer = '' # initialize answer
    for word in brokenSentence:
        answer += english_to_piglatin(word) + " " # add translation and a space

    return answer[:-1]

