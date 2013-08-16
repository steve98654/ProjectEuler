#!/usr/bin/python

from math import factorial

def primes(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

def S(p):
    return sum([factorial(p-k) for k in xrange(1,6)])%p

pmx = 10000        # runs too slow. need to be smarter
plst = primes(pmx)
plst = plst[2:]

print sum([S(p) for p in plst])
