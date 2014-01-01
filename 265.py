import time

mstr = 2**26
mend = 2**27
sm = 0
nchk = []

t1 = time.time()

for n in xrange(mstr,mend):
    if(n%10**6 == 0):
        print (n,sm)
    tpstr   = bin(n)
    tplst   = list(tpstr)
#   lst     = [0]*(34-len(tplst))+ map(int,tplst[2::])
    lst     = [0]*5 + map(int,tplst[2::])
    sublst  = [None]*28
    for i in xrange(28):
        sublst[i] = lst[i:i+5]
   
    sublstfin = sublst + [lst[-5:-1]+lst[0:1],lst[-4:-1]+lst[0:2],\
              lst[-3:-1]+lst[0:3],lst[-2:-1]+lst[0:4]]

    subtup  = tuple(tuple(x) for x in sublstfin)

    if(len(set(subtup))==32):
        sm  = sm+n
        nchk.append(n)

t2 = time.time()

print "Sum"
print sm

print "Timing"
print t2-t1

