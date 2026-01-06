#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 25 10:20:31 2025

@author: rupertjwebb
"""

import random

class domino:
    '''represents an domino
    attributes:
      side1: int from 0 to 7
      side2: int from 0 to 7'''

    def __init__(self, side1, side2):
        '''domino(side1, side2) -> domino
        creates an domino domino with the given side1 and '''
        self.side1 = side1
        self.side2 = side2

    def __str__(self):
        '''str(domino) -> str'''

        return(str(self.side2) + '-' + str(self.side1))


    def is_match(self, other):
        '''domino.is_match(domino) -> boolean
        returns True if the dominoes match in side1 or side2, False if not'''
        return (other.side1 == self.side1) or (other.side1 == self.side2)
    
    def flip(self):
        (self.side1, self.side2) = (self.side2, self.side1)
    

class dominoDeck:
    '''represents a deck of domino dominoes
    attribute:
      deck: list of dominoes'''

    def __init__(self):
        '''dominoDeck() -> dominoDeck
        creates a new full domino deck'''
        self.deck = []
        for i in range(7):
            for j in range(7):
                self.deck.append(domino(i, j))
        random.shuffle(self.deck)  # shuffle the deck

    def __str__(self):
        '''str(dominodeck) -> str'''
        return 'An domino deck with '+str(len(self.deck)) + ' dominoes remaining.'

    def is_empty(self):
        '''dominoDeck.is_empty() -> boolean
        returns True if the deck is empty, False otherwise'''
        return len(self.deck) == 0

    def deal_domino(self):
        '''dominoDeck.deal_domino() -> domino
        deals a domino from the deck and returns it
        (the dealt domino is removed from the deck)'''
        return self.deck.pop()

    def reset_deck(self, pile):
        '''dominoDeck.reset_deck(pile) -> None
        resets the deck from the pile'''
        if len(self.deck) != 0:
            return
        self.deck = pile.reset_pile() # get dominoes from the pile
        random.shuffle(self.deck)  # shuffle the deck

class dominoPile:
    '''represents the disdomino pile in domino
    attribute:
      pile: list of dominoes'''

    def __init__(self, deck):
        '''dominoPile(deck) -> dominoPile
        creates a new pile by drawing a domino from the deck'''
        domino = deck.deal_domino()
        self.pile = [domino]  # all the dominoes in the pile

    def __str__(self):
        '''str(dominoPile) -> str'''
        output = ''
        for domino in self.pile:
            output += str(domino)+','
        return output

    def top_domino(self):
        '''dominoPile.top_domino() -> domino
        returns the top domino in the pile'''
        return self.pile[-1]

    def add_domino(self, domino):
        '''dominoPile.add_domino(domino) -> None
        adds the domino to the top of the pile'''
        self.pile.append(domino)

    def reset_pile(self):
        '''dominoPile.reset_pile() -> list
        removes all but the top domino from the pile and
          returns the rest of the dominoes as a list of dominoes'''
        newdeck = self.pile[:-1]
        self.pile = [self.pile[-1]]
        return newdeck

class dominoPlayer:
    '''represents a player of domino
    attributes:
      name: a string with the player's name
      hand: a list of dominoes'''

    def __init__(self, name, deck, isAI=False):
        '''dominoPlayer(name, deck) -> dominoPlayer
        creates a new player with a new 7-domino hand'''
        self.name = name
        self.hand = [deck.deal_domino() for i in range(7)]
        self.isAI = isAI

    def __str__(self):
        '''str(dominoPlayer) -> dominoPlayer'''
        return str(self.name) + ' has ' + str(len(self.hand)) + ' dominoes.'

    def get_name(self):
        '''dominoPlayer.get_name() -> str
        returns the player's name'''
        return self.name

    def get_hand(self):
        '''get_hand(self) -> str
        returns a string representation of the hand, one domino per line'''
        output = ''
        for domino in self.hand:
            output += str(domino) + '\n'
        return output

    def has_won(self):
        '''dominoPlayer.has_won() -> boolean
        returns True if the player's hand is empty (player has won)'''
        return len(self.hand) == 0

    def draw_domino(self, deck):
        '''dominoPlayer.draw_domino(deck) -> domino
        draws a domino, adds to the player's hand
          and returns the domino drawn'''
        domino = deck.deal_domino()  # get domino from the deck
        self.hand.append(domino)   # add this domino to the hand
        return domino

    def play_domino(self, domino, pile):
        '''dominoPlayer.play_domino(domino, pile) -> None
        plays a domino from the player's hand to the pile
        CAUTION: does not check if the play is legal!'''
        self.hand.remove(domino)
        if domino.side1 == pile.top_domino().side1:
            domino.flip()
        pile.add_domino(domino)

    def take_turn(self, deck, pile):
        '''dominoPlayer.take_turn(deck, pile) -> None
        takes the player's turn in the game
          deck is an dominoDeck representing the current deck
          pile is an dominoPile representing the disdomino pile'''
        # print player info
        if not self.isAI:
            print(self.name + ", it's your turn.")
            print(pile)
            print("Your hand: ")
            print(self.get_hand())
        # get a list of dominoes that can be played
        topdomino = pile.top_domino()
        matches = [domino for domino in self.hand if domino.is_match(topdomino)]
        if len(matches) > 0:  # can play
            if not self.isAI:
                for index in range(len(matches)):
                    # print the playable dominoes with their number
                    print(str(index + 1) + ": " + str(matches[index]))
            # get player's choice of which domino to play
            choice = 0
            if self.isAI:
                choice = 1
            else:
                while choice < 1 or choice > len(matches):
                    choicestr = input("Which do you want to play? ")
                    if choicestr.isdigit():
                        choice = int(choicestr)
                # play the chosen domino from hand, add it to the pile
            self.play_domino(matches[choice - 1], pile)
            topdomino = pile.top_domino()
            if self.isAI:
                print(self.name +' played '+str(topdomino))
        else:  # can't play
            if not self.isAI:
                print("You can't play, so you have to draw.")
                input("Press enter to draw.")
            # check if deck is empty -- if so, reset it
            if deck.is_empty():
                deck.reset_deck(pile)
            # draw a new domino from the deck
            newdomino = self.draw_domino(deck)
            print(self.name+' drew a card')
            if not self.isAI:
                print("You drew: "+str(newdomino))
            if newdomino.is_match(topdomino): # can be played
                if self.isAI:
                    print(self.name+' played what he drew')
                print("Good -- you can play that!")
                self.play_domino(newdomino,pile)
            else:   # still can't play
                if not self.isAI:
                    print("Sorry, you still can't play.")
            if not self.isAI:
                input("Press enter to continue.")
            else:
                topdomino = pile.top_domino()
                print(self.name +' played '+str(topdomino))
        

def play_domino(numPlayers=1,numAI=3):
    '''play_domino(numPlayers) -> None
    plays a game of domino with numPlayers'''
    # set up full deck and initial disdomino pile
    deck = dominoDeck()
    pile = dominoPile(deck)
    # set up the players
    playerList = []
    for n in range(numPlayers):
        # get each player's name, then create an dominoPlayer
        name = input('Player #' + str(n + 1) + ', enter your name: ')
        playerList.append(dominoPlayer(name,deck))
    for a in range(numAI):
        playerList.append(dominoPlayer('AI#'+str(a+1), deck, True))
    # randomly assign who goes first
    currentPlayerNum = random.randrange(numPlayers + numAI)
    # play the game
    while True:
        currentPlayer = playerList[currentPlayerNum]
        # print the game status
        if not currentPlayer.isAI:
            print('-------')
            for player in playerList:
                print(player)
            print('-------')
        # take a turn
        currentPlayer.take_turn(deck, pile)
        # check for a winner
        if currentPlayer.has_won():
            print(currentPlayer.get_name() + " wins!")
            print("Thanks for playing!")
            break
        # go to the next player
        if currentPlayer.isAI:
            input("Press enter to continue.")
        currentPlayerNum = (currentPlayerNum + 1) % (numPlayers + numAI)
play_domino()