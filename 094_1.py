#! /usr/bin/python
# Project Euler problem 94 ported from Mathematica code

# Timing Notes: It takes 21 seconds to go through the first ten million!
# We need to go up to 333 million

# This function works find!  Just takes too long.  Try it in C++.  Test C++ against this.

from math import *
from bigfloat import *
import time

def Ara(lst): 
        s = sum(lst)/2.0
        return sqrt(s*(s-lst[2]))

mxi = 2e6
tol = 1e-8
mxp = 1e9
cnt = 0
prmtot = 0

t1 = time.clock()

#for i in xrange(2,int(mxi+1)):
for i in xrange(2, int(mxi+1)):
    tp1 = Ara([i,i,i-1])
    tp2 = Ara([i,i,i+1])
    t1err = abs(tp1 - round(tp1))
    t2err = abs(tp2 - round(tp2))

    if (t1err < tol and (3*i - 1) < mxp):
        cnt += 1
        prmtot += 3*i - 1
        print ((i,i,i-1), 3*i-1)
    if (t2err < tol and (3*i + 1) < mxp):
        cnt += 1
        prmtot += 3*i + 1
        print ((i,i,i+1), 3*i+1)

t2 = time.clock()

print "Count is: %r. Perm Tot is %r." %(cnt, prmtot)        
print "Total time is %r seconds." % (t2-t1)

