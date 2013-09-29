#! /usr/bin/python end

def F(m, n):
    sol = 1

    if(n>m):
        return sol
    
    for spos in xrange(m-n+1):
        for blen in xrange(n,m-spos+1):
            sol += F(m - spos - blen - 1, n)
    
    return sol

print F(40,3)
