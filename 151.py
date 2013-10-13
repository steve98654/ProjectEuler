#! /usr/bin/env python

# Problem 151 

import numpy as np

def nest(fun,st,n):
    if(n==1):
        return fun(st)
    return nest(fun,fun(st),n-1)

def ItFun(st):
    tk = st[0:4]
    stdr = tk/sum(tk)
    tmp = np.random.multinomial(1,stdr)
    if(sum(tk)==1):
        st[4] += 1
    if((tmp == [1,0,0,0]).all()):
        st += [-1,1,1,1,0]   
    if((tmp == [0,1,0,0]).all()):
        st += [0,-1,1,1,0]
    if((tmp == [0,0,1,0]).all()):
        st += [0,0,-1,1,0]   
    if((tmp == [0,0,0,1]).all()):
        st += [0,0,0,-1,0]   
    return st

if __name__ == "__main__":
    
    np.random.seed(1281) # Let's seed this for simplicity

    cnt = 0
    run = 1000000
    
    for _ in xrange(run):
        st = np.array([1.,1.,1.,1.,0.])
        cnt += nest(ItFun,st,14)[-1]
    
    print cnt, run
    print '%.10f' % float(cnt/run)

# Now see if we can write a C++ version using boost, and crank up the runs
