#testing code
from play import *
from functions import *
from initialization import *

# pile = newPile(1)
# assert sum(pile) == 52
# hList = handList(initHand(pile), pile, 3)
# print(hList)
# prob = callEstimate(pile,hList)
# print(prob)

#game = initGame(3,1)
#print("game, ", game)

#sample = initSample(5, 3, 1)
#print("sample: ", sample)


# print(initGame(3,1))


game = initGame(6,1)
simulateGame(game)
lettuce(game)
print(callEstimate(game[0],game[1][1],1))
print(bustChance(game,1,1))
print(dealerLikely(game,1))
