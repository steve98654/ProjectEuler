# Project Euler problem 131

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

mxp = int(5e4) # largest prime
nmx = int(1e4) # largest n value

pnums = primes2(mxp)
cbs = [i**3 for i in range(2*nmx)]

nlst = array([0])
plst = array([0])

t1 = clock()

# fix an n, compute n**3
#l look through all primes bigger than the last one til we get a match

jfin=1

tstcubs = cbs[1:50]

for n in tstcubs:
    j = jfin
#    while((n**3 + n**2 * pnums[j]) not in cbs and j < len(pnums)-1):
    while((n**3 + n**2 * pnums[j]) not in cbs and j < len(pnums)-1):
        j += 1
        #print "(%r,%r)"%(j,n)
    if(pnums[j] < len(pnums)-1):
        nlst = append(nlst,n)
        plst = append(plst,pnums[j])
        jfin = j

'''
for j in range(1,len(pnums)):
    n = 1
    while(n<nmx and n**3 + n**2 * pnums[j] not in cbs):
        n += 1
        
    if(n**3 + n**2 * pnums[j] in cbs):
        nlst = append(nlst, n)
        plst = append(plst, pnums[j])
'''
t2 = clock()

print nlst
print plst

#plt.plot(plst,nlst)
#plt.show()

print t2-t1
