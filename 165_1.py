# This is not giving us the correct answer! Not sure what is wrong ...
# either an implementation error or our max/min bound checking is not correct

from math import *
from fractions import Fraction
import numpy as np

# arguments are numpy arrays (lists work as well)
def Crs(p1, p2):
    return p1[0]*p2[1]-p1[1]*p2[0]

# arguments are numpy arrays, use a fraction class to store results so that 
# we can easily find results that are redundant later
def IntPt(pt1,pt2,pt3,pt4):
    (p,r,q,s) = (pt1,pt2-pt1, pt3, pt4-pt3)
    if(Crs(r,s) == 0):
        return "None"
    t = Fraction(Crs(q-p,s),Crs(r,s))
    u = Fraction(Crs(p-q,r),Crs(s,r))

    if(t < 1 and t > 0 and u < 1 and u > 0):
        return p+t*r
    else: 
        return "None"

# start random number generation
s = [290797]
t = []

tnum = 20000
for i in xrange(0, tnum+1):
    s.append((s[-1]*s[-1])%50515093)
    t.append(s[-1]%500)

# start brute force search over all pairs of lines 
numlines = 5000
intarr = [];

for i in xrange(0,numlines):
    if(i%50 == 0):
        print i
    for j in xrange(i+1,numlines):
        intarr.append(IntPt(np.array([t[4*i],t[4*i+1]]),np.array([t[4*i+2],t[4*i+3]]), \
                            np.array([t[4*j],t[4*j+1]]),np.array([t[4*j+2],t[4*j+3]])))

# convert to a tuple so that we can apply set
inttup = tuple([tuple(val) for val in intarr])

# find unique intersection points 
tpset = set(inttup)
finum = len(tpset) - 1
print finum

