#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 20:17:27 2024

@author: webbkids
"""

def find(strng, ch, start=0, end=None):
    ix = start
    if end is None:
        end = len(strng)
    while ix < end:
        if strng[ix] == ch:
            return ix
        ix += 1
    return -1