#! /usr/bin/python 
# Project Euler problem 120

import time

nmx = 10000
mxtot = 0

t1 = time.clock()

for a in xrange(3,1001):
    tpr = 0

    for n in xrange(1,nmx):
        r = ((a-1)**n + (a+1)**n)%(a**2)
        if(r > tpr):
            tpr = r
     
    mxtot += tpr
    if(a%10 == 0):
        print a

t2 = time.clock()

print mxtot, t2-t1
        
