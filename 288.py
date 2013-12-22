# Problem 288

# First generate the T sequence 

def T(n,p):  # here n is the number of elements to generate (not T(n) in prob)
    stp = 290797
    t = [] # define T(0)
    for i in xrange(0,n):
        stpn = (stp*stp)%50515093 
        t.append(stp%p)
        stp = stpn
    return t

print T(10,10)
