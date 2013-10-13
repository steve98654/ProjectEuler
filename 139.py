#! /usr/bin/python env

from math import *
from numpy import *

cnt = 0
lim = 1e8
eps = 1e-8
mxvl = 10000; # go to 10000 ultimately 

bsetrp = array([[ (u*u+2*u*v, 2*v*v+2*u*v, u*u+2*v*v+2*u*v) for u in xrange(1,mxvl)]\
        for v in xrange(1,mxvl)])

bsetrp = bsetrp.flatten()
bsetrp = split(bsetrp, len(bsetrp)/3)

for val in bsetrp:
    if(sum(val)<lim and val[2]%(val[1]-val[0])==0):
        cnt += 1

print cnt
