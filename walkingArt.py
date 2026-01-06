#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 17:17:31 2024

@author: webbkids
"""
import turtle
import random
ru = turtle.Turtle()
wn = turtle.Screen()
ru.speed(10)

def random_walk(t,steps):
    for i in range(steps):
        t.forward(random.randint(0, 50))
        t.left(random.randint(-180, 180))
        
random_walk(ru, 10000)
wn.mainloop()

    