from pylab import *
from math import *

# Generate a Lagged Fibonacci pseudo-random sequence of numbers
def LFG(n):
    arr = zeros(n+1,dtype=int)

    for k in xrange(1,min(56,n)):
        arr[k] = (100003 - 200003*k + 300007*k**3)%1000000-500000
   
    if n > 55:
        for k in xrange(56,n+1): 
            arr[k] = (arr[k-24] + arr[k-55] + 1000000)%1000000-500000 
    return arr[1:n+1]

# Find the subarray with the largest sum for a given array of integers using Kadanes's
# algorithm
# This code is taken from http://en.wikipedia.org/wiki/Maximum_subarray_problem
# Here A is a one dimensional array

def max_subarray(A):
    max_ending_here = max_so_far = 0
    #A = map(float,A)
    for x in A:
        max_ending_here = max(0, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far


def arr_decomp_rc(m):
    
    tv = 0
    mtrns = m.T

    for k in arange(0,(int)(sqrt(m.size))):
        t1 = max_subarray(m[k][:])         #rows 
        t2 = max_subarray(mtrns[k][:])     #cols
        tmptv = max(t1,t2)

        if tmptv > tv:
            tv = tmptv

    return tv

def arr_decomp_diag(m):

    tv = 0
    dim = size(m.diagonal())

    for i in xrange(0, dim):
        tpd1 = array([])
        tpd2 = array([])
        tpa1 = array([])
        tpa2 = array([])

        # Main diagonals 
        for k in xrange(0,dim-i):
            tpd1 = append(tpd1, m[k,i+k])
            tpd2 = append(tpd2, m[i+k,k])

        # Anti diagonals
        for k in xrange(0,dim-i):
            tpa1 = append(tpa1, m[dim-k-i-1,k])
            tpa2 = append(tpa2, m[dim-k-1,k+i])

        tmptv = max(max_subarray(tpd1),max_subarray(tpd2),max_subarray(tpa1),max_subarray(tpa2))

        if tmptv > tv:
            tv = tmptv

    return tv

## Begin main code here:

sd = 2000          # only parameter, size of side of random number array

n = sd**2
arr = LFG(n)
mat = arr.reshape(sd,-1)
tpvl1 = arr_decomp_rc(mat)
tpvl2 = arr_decomp_diag(mat)
mxvl  = max(tpvl1, tpvl2)

print mxvl

