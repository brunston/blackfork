import random
import math
from functions import *

#initializes an array of games, [game1, game2, ... , gamen]
def initSample(sampleSize, hands, decks):
    sample = []
    for i in range(sampleSize):
        sample.append(initGame(hands, decks))
    return sample

#initializes an array, [pile, handList]
def initGame(hands, decks):
    #makes a pile
    game = []
    game.append([]) #this becomes game[0], i.e. pile
    game[0] = initPile(decks)
    game.append([]) #this becomes game[1], i.e. handlist
    for i in range(hands):
        game[1].append([])
        for j in range(2):
            dealt = randomCard(game[0])
            #if dealt is 0, do it again, make sure cards exist in the pile to grab
            game[1][i].append(dealt)
            game[0][dealt] = game[0][dealt] - 1
            #update pile
    return game

#initializes a pile
def initPile(decks):
    pile = []
    for i in range(13):
        pile.append(decks*4)
    return pile
