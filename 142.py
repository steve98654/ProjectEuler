#! usr/bin/env python

import math

def sqchk(tmp):
    eps=1e-10
    sqtmp = math.sqrt(tmp)
    return abs(sqtmp-round(sqtmp))<eps

mxsq  = 2000
sq = [i*i for i in xrange(mxsq+1)]
lst = []

for i1 in xrange(1,mxsq):
    if i1%100 == 0:
        print i1
    for i2 in xrange(i1,mxsq):
        for i3 in xrange(i2,mxsq):
            a = sq[i1]
            b = sq[i2]
            c = sq[i3]
            d = a + b - c
            e = c - b
            f = a - c
    
            if(d>0 and e>0 and f>0 and sqchk(d) and sqchk(e) and sqchk(f)): 

                x = (a + b)/2
                y = (e + f)/2
                z = (c - d)/2
            
                tpsum = x + y + z
                if(tpsum > 0 and sqchk(tpsum) and x > 0 and y > 0 and z > 0):
                    lst.append([x,y,z])

print lst
