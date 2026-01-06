#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 13:01:22 2024

@author: webbkids
"""
import turtle

wn = turtle.Screen()
ru = turtle.Turtle()

def square(size, turtle):
    for i in range(4):
        turtle.left(90)
        turtle.forward(size)

square(100, ru)