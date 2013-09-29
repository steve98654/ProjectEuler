from numpy.random import *

# We are getting 0.527 (to 3 digits of accuracy) for our Monte runs 

numgms = int(1e8);
ycnt = 0

for _ in xrange(numgms):
    tpsum = 0

    while(tpsum < 1):
        x = rand()
        tpsum += x
#        print tpsum
    
#    print "x is %r" % x
    while(tpsum < 2):
        y = rand()
        tpsum += y
#        print tpsum

#    print "y is %r" % y
    if(y > x):
        ycnt += 1

print float(ycnt)/numgms        
