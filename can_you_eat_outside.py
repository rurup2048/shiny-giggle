#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 20:27:25 2024

@author: webbkids
"""

def eat_outside(is_sunny, wind):
    '''eat_outside(is_sunny, wind) -> bool
    is_sunny: bool of whether it's sunny or not
    wind: int wind speed in miles per hour
    '''
    return is_sunny and wind < 20
        
        