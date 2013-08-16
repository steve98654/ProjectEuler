# Project Euler problem 131
# Author: Steve Taylor

# http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188

from numpy import *
from time import *
import matplotlib.pyplot as plt

def primes2(n):
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    n, correction = n-n%6+6, 2-(n%6>1)
    sieve = [True] * (n/3)
    for i in xrange(1,int(n**0.5)/3+1):
      if sieve[i]:
        k=3*i+1|1
        sieve[      k*k/3      ::2*k] = [False] * ((n/6-k*k/6-1)/k+1)
        sieve[k*(k-2*(i&1)+4)/3::2*k] = [False] * ((n/6-k*(k-2*(i&1)+4)/6-1)/k+1)
    return [2,3] + [3*i+1|1 for i in xrange(1,n/3-correction) if sieve[i]]

mxp = int(1e6) # largest prime
nmx = int(1e3) # largest n value to construct list of cubes

pnums = primes2(mxp)
cbs = [i**3 for i in range(2*nmx)]

# p must be a difference of cubes follows from math
# a difference of cubes can only be prime if the cubes are consecutive since there is 
# a nontrivial factorization otherwise (follows form algebra) 

pcnt = 0
for i in range(1,len(cbs)):
    ptst = cbs[i] - cbs[i-1]
    if(ptst < 1e6 and ptst in pnums): 
            pcnt += 1
print pcnt
