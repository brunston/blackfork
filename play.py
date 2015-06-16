"""
@title: produce blackjack
@authors: Brunston Poon, Sam Caccavale
@purpose: SPS/AI/2014-2015
"""

import math
import random
from functions import *
from initialization import *
from info import *
#hand is a list
#deck is a list
#card generally represents the value of a card
#Aces = 0
#numerical cards are N-1
#Face cards: Jack = 10, Queen = 11, King = 12

#simulates a game
def simulateGame(game):
    if len(game[1]) > 2:
        for i in range(2,len(game[1])):
            print("deck state: ", game[0])
            print("handList state: ", game[1])
            algorithm(game[1][i], game[0], 17)
    #lettuce(game)
    #...

def main():
    testPile = newPile(1)
    print("testPile:", testPile)
    drawn = randomCard(testPile)
    print("Picked a random card: ", drawn)
    hand = []
    print("Deck after card is drawn: ", deal(testPile, drawn, hand))
    print("Hand value: ", calculateValue(hand))

if __name__ == '__main__':
    test()
