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

def draw_histogram(t, height):
    """ Get turtle t to draw one bar, of height. """
    if height >= 200:
        t.fillcolor("green")
    t.begin_fill()        # Start of the fill area
    t.left(90)
    t.forward(height)     # Draw up the left side
    t.write("  " + str(height))  # Write the data
    t.right(90)
    t.forward(40)         # Width of bar, along the top
    t.right(90)
    t.forward(height)     # And down again!
    t.left(90)            # Put the turtle facing the way we found it.
    t.end_fill()          # Fill in the bar
    t.forward(1)          # Leave small gap after each bar
    t.fillcolor("red")

xs = [] # our data
for v in xs:              # Draw a bar for each number in the data
    draw_bar(tess, v)

wn.mainloop()