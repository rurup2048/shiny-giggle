#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 11 18:10:06 2025

@author: webbkids
"""

class Date:
    '''class to represent a date'''

    def __init__(self,month,day,year):
        '''Date(month,day,year) -> Date'''
        self.month = month
        self.day = day
        self.year = year

    def __str__(self):
        '''str(Date) -> str
        returns date in readable format'''
        # list of strings for the months
        months = ['','Jan','Feb','Mar','Apr','May','Jun','Jul',
                  'Aug','Sep','Oct','Nov','Dec']
        print(self.month)
        output = months[self.month] + ' ' # month
        output += str(self.day) + ', '  # day
        output += str(self.year)
        return output

    def go_to_next_day(self):
        '''Date.go_to_next_day()
        advances the date to the next day'''
        def reset_month():
            self.day = 0
            self.month = (self.month + 1) % len(daysInMonth)
            if self.month == 0:
                self.year += 1
                self.month = 1
        # list with the days in the month
        daysInMonth = [0,31,28,31,30,31,30,31,31,30,31,30,31]
        # check for leap year
        isLeapYear = self.year%4 == 0 and (self.year%100 != 0 or self.year%400 == 0)
        if isLeapYear:
            daysInMonth[2] = 29
    
        if self.day == daysInMonth[self.month]:
            reset_month()

        
        self.day += 1

today = Date(11, 30, 2021)
while True:
    today.go_to_next_day()
    print(today)
    input()
            