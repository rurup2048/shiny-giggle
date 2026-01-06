#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 20:13:12 2024

@author: webbkids
"""

import turtle

turtle.setup(800,600) # Change the width of the drawing to 800px and the height to 600px.
wn = turtle.Screen()
sammy = turtle.Turtle()

inFile = open('mystery.txt','r')
lines = inFile.readlines()
for line in lines:
    print(line)
    lin = line
    if line == "UP\n":
        sammy.penup()
    elif line == "DOWN\n":
        sammy.pendown()
    else:
        lin = line.split()
        print(lin)
        sammy.goto(int(lin[0]), int(lin[1]))
inFile.close()
sammy.hideturtle()
wn.mainloop()
                  