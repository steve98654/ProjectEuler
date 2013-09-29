from math import factorial
from time import *

poword = [1, 1, 170100, 268800, 85050, 4354560, 2100, 311040, 56700, 134400, \
1134, 21772800, 2100, 21772800, 12150, 13440, 42525, 1814400, 60, \
1036800, 34020, 12800, 170100, 10886400, 420, 2177280, 1890, 89600, \
2700, 21772800, 30, 388800, 34020, 33600, 170100, 207360, 1050, \
7257600, 170100, 134400, 17010, 10886400, 300, 4354560, 56700, 10752, \
56700, 5443200, 300, 155520, 4860, 53760, 170100, 2419200, 2100, \
48384, 12150, 8960, 170100, 21772800, 420, 21772800, 56700, 2400, \
28350, 54432, 1050, 3110400, 4860, 268800, 4860, 3628800, 2100, \
3628800, 17010, 53760, 34020, 3110400, 700, 777600, 180, 67200, 1260, \
21772800, 300, 4354560, 170100, 134400, 170100, 3628800, 70, 1036800, \
170100, 53760, 85050, 544320, 2100, 388800, 8100, 2560, 567]

f15o = 217728000             # period of fib nums mod 15!
sumremainder = 116992000
#f15o = 100 #test line only
#sumremainder = 50 # test line only
fact = factorial(15)
reps = 4592886 # number reps of fib num period til we are just less than 10^15
               # total terms in sum is reps*f15o + sumremainder + 1
fvec = [0,1]

t1 = clock()

## THIS SEEMS TO BE THE SAME THING WE ARE GETTING IN C++ CODE
# build fib numbers mod 15! out to f15o
for i in xrange(2,f15o):  # start at 2 stop at end-1, takes around 40secs 
    fvec.append((fvec[i-1] + fvec[i-2])%fact)
    
t2 = clock()

## PROBLEM IS THE FOLLOWING, LET X = 100 SO THAT XMODTP = {1,100,10000, ..}
## ON THE FIRST LOOP, BUT IS SOMETHING DIFF ON NEXT LOOP, E.G. 
## {716324608000, ....}  NEED TO ADD MORE ELEMENTS TO PERIOD

buf = 40 # compute powermod 40 steps after period
## overwrite first buf elements of poword array after first pass through loop

outsum = 0 #final sum

for x in xrange(1,101):  #don't start at 0, since 0^0=1 in python

    if(x == 25):
        buf = 25  # shorten buffer when numbers get big enough

    xmodtp = []   # compute power mod up to the value where it repeats 
    for n in xrange(0,poword[x]+buf):
        xmodtp.append(pow(x,n,fact))

    # compute sum out to first rep of Fib numbers f15u
    tpsum = 0
    
    # compute first sum

    firstsum = 0;

    for k in xrange(0,f15o):
        firstsum += (fvec[k]*xmodtp[k%poword[x]])%fact

    #overwrite first values of xmodtp to account for higher numbers
    xmodtp[0:buf] = xmodtp[poword[x]:poword[x]+buf]
    
    # compute remainder sum, and rep sums

    for k in xrange(0,sumremainder+1): # need plus one since <= n
        tpsum += (fvec[k]*xmodtp[k%poword[x]])%fact
        
    rmsum = tpsum%fact

    for k in xrange(sumremainder+1,f15o): 
        tpsum += (fvec[k]*xmodtp[k%poword[x]])%fact

    finsum = tpsum%fact

    outsum += (firstsum + (reps-1)*finsum + rmsum)%fact
    #print x, rmsum, finsum, outsum, len(xmodtp)
    print x, outsum
    
t3 = clock()

#print xmodtp[0:50]
print rmsum, finsum, outsum%fact
print t3-t1, t3-t2, t2-t1
