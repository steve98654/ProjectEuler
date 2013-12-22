# Problem 282

import numpy as np

# define the function
def A(m,n):
    if(m == 0):
        return n+1
    elif(m > 0 and n == 0):
        return A(m-1,1)
    else: 
        return A(m-1,A(m,n-1))

# matrix to store values 
Astr = np.zeros((7,7))

for i in xrange(0,4):
    for j in xrange(0,7):
        Astr[i][j] = A(i,j)

# now lets try to think of a way to compute the fifth row A(4,i). 

print Astr

