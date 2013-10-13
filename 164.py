#! /usr/bin/env python

import numpy as np

dgts = 20
tab = np.zeros((10,10,dgts+1))

def ForIt(i1, i2, depth):
    if(depth == 0):
        return 1
    else:
        if(tab[i1][i2][depth]==0):
            res = 0
            for i in xrange(0,10-i2-i1):
                tab[i1][i2][depth] += ForIt(i2,i,depth-1)
        return tab[i1][i2][depth]

if __name__ == "__main__":
    cnt = 0

    for i1 in xrange(1,10):
        for i2 in xrange(0,10-i1):
            cnt += ForIt(i1,i2,dgts-2)
            print cnt

print "%f" % cnt

