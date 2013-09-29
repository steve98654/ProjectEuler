#! /usr/bin/env python

from time import clock

def rwh_primes1(n):
    # http://stackoverflow.com/questions/2068372/
    # fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns  a list of primes < n """
    sieve = [True] * (n/2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]

dgts = 6
stp2 = 10**(dgts)

#prime generation
t1 = clock()
plst = rwh_primes1(stp2)
plst = filter(lambda x:x>10**(dgts-1),plst)
t2 = clock()

#check and separate

print t2 - t1
print plst[0], plst[-1]
