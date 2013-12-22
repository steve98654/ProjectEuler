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

def uprime_factors(n, primelist):
    if primelist is None:
        primelist = primes2(n)
 
    fs = []
    for p in primelist:
        count = 0
        while n % p == 0:
            n /= p
            count += 1
        if count > 0:
            fs.append((p, count))
 
    rs = [i[0] for i in fs]
    return rs

def next_prime(n, primelist):
    """ Finds the next prime in primelist larger than n """
    if primelist is None:
        primelist = primes2(n)

    return primelist[bisect_right(primelist, n)]
    
def chk_consq_pfac(n, primelist):
    """ Check if fctlst is a list of consecutive primes in primelist""" 
    fctlst = uprime_factors(n,primelist)
    pmin = fctlst[0]
    ind = primelist.index(pmin)
    return primelist[ind + len(fctlst) -1] == fctlst[-1]

maxN = int(1e4)
maxpm = int(1e6+1e5)  # maximum prime 
plst = primes2(maxpm)


powtwo = [2**n for n in range(1,30)]
adnums = []

for n in xrange(1,maxN/2+1):
    if(2*n not in powtwo and chk_consq_pfac(2*n,plst)):
        adnums.append(2*n)

adnums = sorted(adnums + powtwo)

print adnums
#print uprime_factors(100,plst)
#print next_prime(1000000, plst)

#  This seems to be going to slow.  I need to build the admissible numbers directly
#  by taking subsets of consec primes, then taking all powers of the 
#  corresponding integers while keeping the number less than a billion. Note that 
#  they all must have a 2 in them!!

