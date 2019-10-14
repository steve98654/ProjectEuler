def maxPrimeDivisor(n): 
      
    # Returns Maximum Prime  
    # Divisor of n 
    MPD = -1
      
    if n == 1 :  
        return 1
      
    while n % 2 == 0: 
        MPD = 2
        n = n // 2
      
    # math.sqrt(n) + 1 
    size = int(n ** 0.5) + 1
    for odd in range( 3, size, 2 ): 
        while n % odd == 0: 
              
            # Make sure no multiples  
            # of prime, enters here 
            MPD = odd 
            n = n // odd 
      
    # When n is prime itself 
    MPD = max (n, MPD)  
      
    return MPD 

cnt = 1
from math import sqrt
mxvl = 100000
for i in range(1,mxvl + 1):
    if maxPrimeDivisor(i) < sqrt(i):
        cnt = cnt + 1
        

print cnt
