import time
import os 
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

class Player():
    '''the main player in the game'''
    def __init__(self, stats)