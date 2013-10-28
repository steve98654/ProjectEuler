from math import sqrt,atan,pi

k1 = (8 - 4*sqrt(5) + 9*atan(1/(4*sqrt(5))))/8

def f(k):
    sq1 = sqrt(4*k*k-4*k-3)
    sq2 = sqrt(4*k*(1+k)-3)

    return (2*(sq1-sq2+k*pi)+(1-2*k)**2*atan(2/sq1)-(1+2*k)**2*atan(2/sq2))/(4*k*k)

mxvl = 100000

print sum([k*f(k) for k in xrange(2,mxvl+1)])+k1

