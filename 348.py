#! /usr/bin/env python

import numpy as np

sqmx = 2500
cbmx = 200

num = [i*i + j*j*j for i in xrange(sqmx) for j in xrange(cbmx)]

lst = []

for n in num:
    stn = str(n)
    if stn == stn[::-1]:
        lst.append(n)

cnt = {}
fin = []

for i in set(lst):
    if(num.count(i) == 4):
        fin.append(i)
#        cnt[i] = num.count(i)

print fin

