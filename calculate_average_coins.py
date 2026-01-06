#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  9 18:50:31 2025

@author: webbkids
"""

def calculate_average_coins(coin_values):
    """
    Calculates the average number of coins needed to make change with given coin values.
    
    Args:
        coin_values: A list of integer coin values.
    
    Returns:
        The average number of coins needed.
    """
    total_coins = 0
    for amount in range(100):
        min_coins = float('inf')
        for value in coin_values:
            if amount >= value:
                remaining = amount - value
                min_coins = min(min_coins, 1 + calculate_average_coins([value]) if remaining == 0 else 1 + calculate_average_coins([value]))
        total_coins += min_coins
    return total_coins / 100 

def find_best_coinage():
    """
    Finds the combination of 3 coin values that minimizes the average number of coins needed.
    
    Returns:
        A list of the 3 best coin values.
    """
    best_avg = float('inf')
    best_coins = []
    for i in range(1, 50):
        for j in range(i + 1, 50):
            for k in range(j + 1, 50):
                avg_coins = calculate_average_coins([i, j, k])
                if avg_coins < best_avg:
                    best_avg = avg_coins
                    best_coins = [i, j, k]
    return best_coins

# Example usage
print("The best coin combination is:", find_best_coinage()) 