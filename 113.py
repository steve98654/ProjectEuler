#! /usr/bin/env python

from scipy.misc import comb
#from numpy import factorial

# n is total digits
# m is num of digits less than n

def cntord(n,m):
    return comb(n+m-1,m)

tvls = 0
dgtsz = 5

for m in xrange(0,10):
    tvls += cntord(dgtsz,m)

print tvls

print cntord(6,10)

m = 6
n = 10
tot = 0

for m in xrange(0,5): tot += cntord(n+m-1,m)

print tot

cnt = 0
for i1 in xrange(1,10):
    for i2 in xrange(i1,10):
        for i3 in xrange(i2,10):
            for i4 in xrange(i3,10):
                for i5 in xrange(i4,10):
                    cnt += 1
                    print (i1, i2, i3, i4, i5)

print cnt
