#! /usr/bin/env python

import numpy as np
from math import cos,pi

# Get nbrs of a point in cubic coordinates 
def Nbrs(lst):
    return lst + np.array([[1,-1,0],[1,0,-1],[0,1,-1],[-1,1,0],[-1,0,1],[0,-1,1]])

print Nbrs(np.array([1,-1,0])) # Example usage of nbrs 


tvl = 2*np.array([0 -1 -1])

gdlst = [9, 10404, 16900, 97344]

res = []

for i in gdlst:
    for j in range(2):
        res.append(tvl)
        tvl = Nbrs(tvl)


xgrd = np.array(range(-2,2))
ygrd = np.array(range(-2,2))
r = 1

xctr =  r * cos(pi)*(2*xgrd-ygrd)
yctr = -ygrd * (r*3/2)

print tvl
print xctr, yctr


## Choose and initial direction

ini = [-1, 1, 0]
nxt = ini
nxt[1]--; x[3]++

# take nbrs, of ini whos abs sum is equl to ini. 
# construct both initial scaled value and nbr to the right


