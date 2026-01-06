#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 10:59:19 2024

@author: webbkids
"""

import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color("blue")
tess.fillcolor("red")

def draw_bar(t, height):
    """ Get turtle t to draw one bar, of height. """
    if height >= 200:
        t.fillcolor("green")
    t.begin_fill()        # Start of the fill area
    t.left(90)
    t.forward(height)     # Draw up the left side
    t.write("  " + str(height))  # Write the data
    t.right(90)
    t.forward(4)         # Width of bar, along the top
    t.right(90)
    t.forward(height)     # And down again!
    t.left(90)            # Put the turtle facing the way we found it.
    t.end_fill()          # Fill in the bar
    t.forward(1)         # Leave small gap after each bar
    t.fillcolor("red")

xs = [3, 2, 1, 0, 7, 6, 5, 4, 11, 10, 9, 8, 15, 14, 13, 12, 19, 18, 17, 16, 23, 22, 21, 20, 27, 26, 25, 24, 31, 30, 29, 28, 35, 34, 33, 32, 39, 38, 37, 36, 43, 42, 41, 40, 47, 46, 45, 44, 51, 50, 49, 48, 55, 54, 53, 52, 59, 58, 57, 56, 63, 62, 61, 60, 67, 66, 65, 64, 71, 70, 69, 68, 75, 74, 73, 72, 79, 78, 77, 76, 83, 82, 81, 80, 87, 86, 85, 84, 91, 90, 89, 88, 95, 94, 93, 92, 99, 98, 97, 96] # our data
tess.setheading(180)
tess.forward(300)
tess.setheading(0)
for v in xs:              # Draw a bar for each number in the data
    draw_bar(tess, v)

wn.mainloop()