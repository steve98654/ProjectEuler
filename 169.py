from math import *
import sys

sys.setrecursionlimit(10000)


#@memoise 
def Vals(n,i,j):
    if(j > 0 and 2**i <= n and n < 2**i*(j+2) and i > 0): 
        return Vals(n,i-1,2) + Vals(n-2**i,i,j-1)
    elif(i>0): 
        return Vals(n,i-1,2)
    else:
        return bool(n==0)

n = 10**3

print Vals(n,floor(log(2,n)),2)
    
