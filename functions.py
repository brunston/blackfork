from __future__ import division
from random import *
#...(former location of probability as a FN GLOBAL)

#OUR SUPERCOOL GENETIC MUTANT NINJA TURTALGORITHM
def genetics(sampleList):
    winLoss = [] #win/loss arrays for each sample
    for sample in range(sampleList):
        winLoss.append(isWinSample(sampleList[sample]))

#The algorithm which dictates what our hand does
#bustThreshold is the determinant for whether we hit or stay
def lettuce(game, bustThreshold=0.5):
    print("Pile given to lettuce", game[0])
    # value = calculateValue(hand)
    # if value < threshold:
    #     newCard = randomCard(pile)
    #     deal(pile, newCard, hand)
    # if value >= threshold:
    i = 0
    dealer = dealerLikely(game, 1)
    while dealerLikely < 17:
        print("in dealerLikely loop in lettuce")
        i += 1
        dealer = dealerLikely(game, i)
        #Used to make sure that we get accurate numbers for when the dealer
        #algo actually stays.
    print("Pile after dealerLikely loop" , game[0])
    handValue = calculateValue(game[1][1]) #our hand
    equation = ((handValue - dealer[0]))
    if equation <= 0: #dealer likely is higher
        #deal the hand
        if bustChance(game, 1, 1) <= bustThreshold:
            print("attempting to deal to me")
            deal(game[0],randomCard(game[0]),game[1][1])
            print("Game before lettuce round", game)
            lettuce(game) #recursive where it will continue until
    print("pile after recursion", game[0])
    dealerValue = calculateValue(game[1][0])
    print("right before deathloop")
    while dealerValue < 17:
        print("in dealerValue/algorithm loop in lettuce")
        print("pile prior to algorithm", game[0])
        algorithm(game[1][0],game[0])
        print("dealer hand:", game[1][0])
        dealerValue = calculateValue(game[1][0])


    #things we need
    #a 'goodness equation" which can be run for each sample in our simulation
    #we can use a function which creates an array of True/False for wins or losses
    #a semi-random generator which selects what hands to hit on and stay
    #beginning with simple hit/stay on 15,16,17 etc
    #continuing onto dealing with percentages given certain


#returns a list with [highest probable dealer hand value, percentage of getting that value]
def dealerLikely(game, cards, handNum = 0):

    probabilityList = callEstimate(game[0],game[1][handNum], cards)
    print("pile in dealerLikely", game[0])
    highestProbableValue = 0
    for i in probabilityList:
        if probabilityList[i] > highestProbableValue:
            highestProbableValue = i
    percentage = probabilityList[i]
    return [highestProbableValue, percentage]

#Returns a float that is the chance of busting
def bustChance(game, handNum, cards):
    bustList = callEstimate(game[0], game[1][handNum], cards)
    print("This is bust list ", bustList)
    bust = 0
    notBust = 0
    for i in range(len(bustList)):
        if i < 21:
            notBust = notBust + bustList[i]
        else:
            bust = bust + bustList[i]
    print(bust)
    print(notBust)
    return bust/(bust + notBust)


#returns the total number of cards in the pile
def total(pile):
    total = 0
    for i in range(len(pile)):
        total = total + pile[i]
    return total

#creates a list of hands incl dealer and initializes the non-dealer hands
def handList(dealer, pile, numhands):
    handList = []
    handList.append(dealer)
    for i in range(numhands):
        handList.append(initHand(pile))
    return handList

#Give it a pile, hand, and the amount of cards to deal
#Returns an array where the index is the value of the hand and the value is the chance of getting it
def callEstimate(pile, hand, numberOfCards):
    probability = []
    print("pile in callestimate", pile)
    for i in range((len(hand) + 1) * 11):
        probability.append(0)
    pileEstimate = pile
    estimate(calculateValue(hand), pileEstimate, numberOfCards, probability)
    print("pile after estimate / for loop in callestimate", pile)
    return probability

def estimate(value, pile, cards, probability):
    newpile = pile
    print("pile in estimate", cards, "newpile:", newpile)
    if cards == 0:
        probability[value] = probability[value] + 1
        return probability
    else:
        for i in range(0,13):
            while newpile[i] > 0:
                newpile[i] = newpile[i] - 1
                probability = estimate(value + calculateValue([i]), newpile, cards - 1, probability)


#changable algorithm default to soft 17 hit, updating dealer's hand / dealer decision algorithm
def algorithm(hand, pile, threshold = 17):
    print("algorithm start pile", pile)
    value = calculateValue(hand)
    while value < threshold:
        value = calculateValue(hand)
        print("pile before randomCard", pile)
        newCard = randomCard(pile)
        deal(pile, newCard, hand)

#chooses a random card from the pile, value 0-12
#DON'T TOUCH
def randomCard(pile):
    print("totalpile:",total(pile))
    goal = randrange(0,total(pile))
    card = 0
    if goal < pile[0]:
        return 0
    while goal >= pile[card]:
        goal = goal - pile[card]
        card = card + 1
    return card

#removes a card from the pile, value 0-12
def deal(pile, card, hand):
    if pile[card] > 0:
        pile[card] = pile[card] - 1
        addToHand(hand, card)
    else:
        return None

#adds a card to hand
def addToHand(hand, card):
    hand.append(card)
    return hand

#calculates value of a hand
#figure out how to deal with an Ace (card = 0)
def calculateValue(hand):
    total = 0
    aces = 0
    for i in hand:
        if i == 10: #jack
            total = total + 10
        elif i == 11: #queen
            total = total + 10
        elif i == 12: #king
            total = total + 10
        elif i == 0: #ace
            total = aces + 1
        else:
            total = total + (i+1)
    return total

#Given threshold, returns True to hit, False to stay
#need to make it possible to get probability of going over
def hitStay(threshold, pile, card):
    probability = chance(pile, card)
    if probability >= threshold:
        return True #hit
    else:
        return False #stay

#calculates probability of drawing a card from the pile
def chance(pile, card):
    probability = amount(pile, card) / total(pile)
    return probability

#returns the number of a specific kind of card in the pile
def amount(pile, card):
    return pile[card]


#checks each hand in handList to see if it has busted, returns true if over.
def checkList(handList):
    busted = []
    for hand in handList:
        if calculateValue(hand) <= 21:
            busted.append(False)
        else:
            busted.append(True)
    return busted


def isWin(game):
    if calculateValue(game[1][1]) > calculateValue([1][0]):
        return True
    else:
        return False

def isWinSample(sample):
    winList = []
    for i in sample:
        winList.append(isWin(sample[i]))
    numberWon = []
    numberLost = []
    for j in winList:
        if winList == True:
            numberWon += 1
        else:
            numberLost += 1
    return [numberWon, numberLost]
