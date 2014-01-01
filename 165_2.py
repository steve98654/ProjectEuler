# This is not giving us the correct answer! Not sure what is wrong ...
# either an implementation error or our max/min bound checking is not correct

from math import *
from fractions import Fraction

def all_indices(value, qlist):
    indices = []
    idx = -1
    while True:
        try:
            idx = qlist.index(value, idx+1)
            indices.append(idx)
        except ValueError:
            break
    return indices

def IntPt(x1, y1, x2, y2, x3, y3, x4, y4):
    denom = (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)
    if(denom == 0):
        return ('Inf', 'Inf')
    f1 = (x1*y2 - y1*x2)
    f2 = (x3*y4 - y3*x4)
    Px = Fraction((f1*(x3-x4) - (x1-x2)*f2),denom)
    Py = Fraction((f1*(y3-y4) - (y1-y2)*f2),denom)
    tst1 = [Px > x1, Px > x2, Px > x3, Px > x4]
    tst2 = [Py > y1, Py > y2, Py > y3, Py > y4]

    if(len(all_indices(True,tst1)) == 0 or len(all_indices(True,tst2)) == 0):
        return ('None', 'None')
    if(len(all_indices(True,tst1)) == 2 and len(all_indices(True,tst2)) == 2):
        return (Px, Py)
    else:
        return ('None', 'None')

s = [290797]
t = []

tnum = 20000
for i in xrange(0, tnum+1):
    s.append((s[-1]*s[-1])%50515093)
    t.append(s[-1]%500)

numlines = 5000
intarr = [];

for i in xrange(0,numlines):
    if(i%50 == 0):
        print i
    for j in xrange(i+1,numlines):
        intarr.append(IntPt(t[4*i], t[4*i+1], t[4*i+2], t[4*i+3], \
                t[4*j], t[4*j+1], t[4*j+2], t[4*j+3]));

tpset = list(set(tuple(intarr)))
finum = len(tpset) - 2
print finum

