#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 12:26:17 2024

@author: webbkids
"""
import turtle

wn = turtle.Screen()
ru = turtle.Turtle()

size = 9
def square(size, turtle):
    for i in range(4):
        turtle.left(90)
        turtle.forward(size)
       
for i in range (size):
    square(i * 50, ru)
    
    ru.penup()
    ru.forward(25)
    ru.right(90)
    ru.forward(25)
    ru.left(90)
    ru.pendown()
wn.mainloop()