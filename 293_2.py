import pickle 
from bisect import bisect_right

def primes2(n):
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    correction = (n%6>1)
    n = {0:n,1:n-1,2:n+4,3:n+3,4:n+2,5:n+1}[n%6]
    sieve = [True] * (n/3)
    sieve[0] = False
    for i in xrange(int(n**0.5)/3+1):
      if sieve[i]:
        k=3*i+1|1
        sieve[      ((k*k)/3)      ::2*k]=[False]*((n/6-(k*k)/6-1)/k+1)
        sieve[(k*k+4*k-2*k*(i&1))/3::2*k]=[False]*((n/6-(k*k+4*k-2*k*(i&1))/6-1)/k+1)
    return [2,3] + [3*i+1|1 for i in xrange(1,n/3-correction) if sieve[i]]

def next_prime(n, primelist):
    """ Finds the next prime in primelist larger than n """
    if primelist is None:
        primelist = primes2(n)

    return primelist[bisect_right(primelist, n)]
    

cnms = sorted(pickle.load(open("anums2.p",'rb')))
maxpm = int(1e9+1e4)  # maximum prime 
plst = primes2(maxpm)

pF = []

for n in cnms:
    pF.append(next_prime(n+1, plst) - n)

print sum(list(set(pF)))

