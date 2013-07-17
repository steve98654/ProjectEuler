import numpy as np
from bigfloat import *

def pval(n,k):

    with precision(100000):
            return pow(div(n,k),k)
        
def find_all(a_str, sub): 
    start = 0
    while True: 
        start = a_str.find(sub, start)
        if start == -1: return
        yield start 
        start += len(sub)

with precision(100000): 

    DCST = 990   # number of nonzero digits to be large
    d = 0
    kmx = 2

for n in xrange(5,10001):
    
    tp = 0
    
    for k in xrange(kmx,kmx+2):
        x = pval(n,k)
        if x >= tp:
            tp = x
            kmx = k

    outzrs   = list(find_all(str(tp)[-1000:], '0'))
    outzrs1  = list(find_all(str(tp)[-1000:], '9'))

    narr    = np.asarray(outzrs)
    narr2   = np.asarray(outzrs1)
    
    if len(narr) > DCST:
        d -= n
    elif len(narr2) > DCST:
        d -= n
    else:     
        d += n

    print "%r: %r: %r" % (n,d,kmx)
