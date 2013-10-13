import numpy as np
from operator import mul 

def baseN(num,b,numerals="0123456789abcdefghijklmnopqrstuvwxyz"):
    return ((num == 0) and numerals[0]) or (baseN(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])

tot = 0
mxrow = 1000000000

for i in xrange(0,mxrow):
    if(i%1000000==0):
        print i/1000000

    vl = baseN(i,7)
    vlstr = np.array([int(i)+1 for i in str(vl)])
    tot += reduce(mul,vlstr,1)

print tot

