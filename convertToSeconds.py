#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 11:09:27 2024

@author: webbkids
"""

def convert_to_seconds( hours, minutes, seconds):
    ''' convert the time to seconds '''
    secondsTotal = (hours * 3600) + (minutes * 60) + seconds
    return secondsTotal

print(convert_to_seconds(2, 30, 15))