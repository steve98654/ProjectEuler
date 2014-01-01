from math import *

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

def parm(x0, y0, x1, y1, x2, y2, x3, y3):
    denom = float((x3-x2)*(y0-y1) + (x0-x1)*(y2-y3))

    if(abs(denom) < 1e-10): # case when lines are parallel
        return 0
    else:
        s = (x2*(y1-y0)+x1*(y0-y2)+x0*(y2-y1))/denom
        if(s > 0 and s < 1):
            if(x0 != x1):
                t = (x0 - x2 + s*(x2-x3))/(x0-x1)
            else:
                t = (y0 - y2 + s*(y2-y3))/(y0-y1)

            if(t > 0 and t < 1):
                return ((x1-x0)*t + x0, (y1-y0)*t + y0)           # return intersection pt here
            else:
                return 0
        else:
            return 0

s = [290797]
t = []

tnum = 20000
for i in xrange(0, tnum+1):
    s.append((s[-1]*s[-1])%50515093)
    t.append(s[-1]%500)

numlines = 5000
intarr = [];

for i in xrange(0,numlines):
    for j in xrange(i+1,numlines):
        intarr.append(parm(t[4*i+1], t[4*i+2], t[4*i+3], t[4*i+4], \
                t[4*j+1], t[4*j+2], t[4*j+3], t[4*j+4]));

tpset = list(set(tuple(intarr)))
tplst = []

for x in tpset:
    if(isinstance(x,int) == False):
        tplst.append(list(x))

sortints = sorted(tplst, key = lambda a_entry: a_entry[0]) # sort x values 
sxvls = [x[0] for x in sortints]

xrep = []

for i in xrange(0,len(sxvls)-1):
    if(abs(sxvls[i+1]-sxvls[i]) < 1e-10):
        xrep.append(sxvls[i])

uxrep = sorted(list(set(xrep)))
dupcnt = 0

for uval in uxrep:
    tpinds = all_indices(uval,sxvls)
    if(len(tpinds) > 1):
        ltmp = [sortints[ind][1] for ind in tpinds]
        dupcnt = dupcnt + len(ltmp) - len(set(ltmp))
