# Project Euler problem 84

import random as rn
import numpy as np

# Class to represent a deck of chance and community chest cards 
# Note that the cards are randomly shuffled 
# see the problem statement for definitions of what cards mean
class deck:
    def __init__(self, sd):
        self.seed = sd

        rn.seed(sd)
        crds = [i for i in xrange(1,16)]
        rn.shuffle(crds)
        self.cards = crds

    def drawcard(self):
        tplst = self.cards[1:16]
        tplst = np.append(tplst,self.cards[0])
        self.cards = tplst

# Given a community chest card car and the current square 
# return the square where the card says to go 
def ccsub(crd, sqr):
    if crd == 1:
        rtsqr = 0
    elif crd == 2:
        rtsqr = 10
    else:
        rtsqr = sqr
    return rtsqr

# Given a chance card crd and the current square sqr, 
# return the square where the card says to go
def chsub(crd, sqr): 
    if crd == 1:
        rtsqr = 0
    elif crd == 2:
        rtsqr = 10
    elif crd == 3:
        rtsqr = 11
    elif crd == 4:
        rtsqr = 24
    elif crd == 5:
        rtsqr = 39
    elif crd == 6:
        rtsqr = 5
    elif (crd == 7 or crd == 8):
        if sqr == 7:
            rtsqr = 15
        elif sqr == 22:
            rtsqr = 25
        else: 
            rtsqr = 5
    elif crd == 9:
        if (sqr == 7 or sqr == 36):
            rtsqr = 12
        elif sqr == 22:
            rtsqr = 28
    elif crd == 10:
        rtsqr = sqr - 3
    else:
        rtsqr = sqr 
    return rtsqr     
                
# Construct a deck of chance and community chest cards
# arguments are random number generator seeds 
chcrds = deck(11)
cccrds = deck(321)

sqhits = np.zeros(40) # vector to keep track of hits 
cursqr = 0 # initial square 
sqhits[0] = sqhits[0] + 1 # note that we are on the initial square 

die_sides = 4
d1 = 1; d2 = 2
d1p = 1; d2p = 2
d1pp = 1; d2pp = 2
fsqr = 0
## begin main simulation

dbug = 0 # debug flag
mxrolls = int(1e6)  # max number of rolls 

for kk in xrange(1, mxrolls):
    
    d1pp = d1p
    d2pp = d2p
    d1p = d1
    d2p = d2
    d1  = rn.randint(1, die_sides)
    d2  = rn.randint(1, die_sides)
	
    tpsqr = fsqr + d1 + d2  # find next square  
    tpsqr = np.mod(tpsqr, 40) # mod by 40 to stay on the board
	
    if ((d1 == d2 and d1p == d2p and d1pp == d2pp) or tpsqr == 30):
        fsqr = 10
        d1 = 1; d2 = 2 # reset the doubles if we go to jail
        if dbug == 1:
            print "Doubles %r %r %r %r %r %r %r" % (d1, d2, d1p, d2p, d1pp, d2pp, tpsqr)
    elif (tpsqr == 7 or tpsqr == 22 or tpsqr == 36):
        fsqr = chsub(int(chcrds.cards[0]),tpsqr)
        if dbug == 1:
            print fsqr
        chcrds.drawcard()
    elif (tpsqr == 2 or tpsqr == 17 or tpsqr == 33): 
        fsqr = ccsub(int(cccrds.cards[0]),tpsqr)
        if dbug == 1:
            print fsqr
        cccrds.drawcard() 
    else:
        fsqr = tpsqr
    
    fsqr = np.mod(fsqr,40) # mod out by 40 just in case we went around the board
    sqhits[fsqr] = sqhits[fsqr] + 1 # increment the square counter

outarr = sqhits/mxrolls
print outarr.argsort()[-3:][::-1]
