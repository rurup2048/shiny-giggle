#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 20:44:41 2025

@author: webbkids
"""

def print_stacks(position):
    '''print_stacks(position) -> str
    return string represent the stacks in position
    '''
    # get maximum height of the stacks
    height = max([len(stack) for stack in position])
    outString = '\n'  # output string -- start with newline

    for level in range(height-1,-1,-1): # print from top to bottom
        for stack in position:
            if level < len(stack):
                outString += str(stack[level]) # print a disc
            else:
                outString += ' '  # leave a space
            outString += ' ' # go to the next stack
        outString += '\n'   # go to the next row
    outString += '- - -\n' # bases of the stacks

    return outString

def move_disc(position, start, goal):
    '''move_disc(position, start, goal)
    moves a disc from stack "start" to stack "goal"
    '''
    disc = position[start].pop()
    position[goal].append(disc)

def solve_hanoi(position, size, start, goal):
    '''solve_hanoi(position, size, start, goal)
    solves Towers of Hanoi problem on position
    move stack of size "size" from start peg to goal peg
    '''
    third = 3 - (start + goal)  # this is the third stack

    if size > 1:
        # first step of recursion -- move stack of size
        # size - 1 to the third stack
        solve_hanoi(position, size - 1, start, third)

    # move bottom disc and print current state
    move_disc(position, start, goal)
    print(print_stacks(position))

    if size > 1:
        # second step of recursion -- move stack of size
        # size - 1 onto the goal stack
        solve_hanoi(position, size - 1, third, goal)

position = [[8, 7, 6, 5, 4, 3, 2, 1], [], []]  # start position
print(print_stacks(position))
solve_hanoi(position, 8, 0, 2)