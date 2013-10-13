import numpy as np
import math

vls = []

gdlst = [9, 10404, 16900, 97344]

nmx = 10000

#for n in range(nmx):
for n in gdlst:
    for d in range(1,n):
        q = n/d
        r = n%d
        vec = np.sort(np.array([d, q, r]))
#        vec = np.array([r,d,q])
        if(vec[0]!=0 and float(vec[2])/vec[1] == float(vec[1])/vec[0]):
            vls.append([n, r, d, q])

sqvls = []

for num in vls:
    sq = math.sqrt(num[0])
    if(abs(sq - int(sq))<1e-8):
        sqvls.append(num)

print sqvls
