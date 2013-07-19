#! /usr/bin/python
import time
import math

def cnsols2(l, w, h): 
    return min([math.sqrt(l*l + (h+w)*(h+w)), math.sqrt(h*h + (l+w)*(l+w)),
            math.sqrt((h+l)*(h+l)+w*w)])

def rtcnt(mxend):
    cnt = 0
    tol = 1e-8
    for l in xrange(1,mxend+1):
        for w in xrange(l,mxend+1):
            for h in xrange(w,mxend+1):
                vl = cnsols2(l,w,h)
                if abs(vl - round(vl))<tol:
                    cnt+=1
        if l%50 is 0:
            print l
    return cnt

mxstr = 100
mxend = 2000
tvl = 1e6

# define mxmid = mean(mxstr,mxend)
# if lower than tvl, then mxmid = mean(mxmid,mxend)
# if higher then mxmid = mean(mxmid,mxstr)
# keep iterating this 

# compute for mxstr, if less than tvl try for 

t1 = time.clock() 

print rtcnt(mxstr)
print cnsols2(34,76,100)

t2 = time.clock()

print t2-t1
