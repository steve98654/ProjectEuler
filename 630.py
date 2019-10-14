import numpy as np 

S = 290797
k = 2500
T = []

for i in range(2*k+1):
    T.append(S%2000-1000)
    S = (S*S)%50515093

pts = np.array(T[1:]).reshape(k,2).astype(float)

slps = []
ints = []

print "start"

for i,pt1 in enumerate(pts):
    for j,pt2 in enumerate(pts):
        if i != j:
            if np.abs(pt2[0] - pt1[0]) < 0.0000000001:
                slp = 1000000000
                ctp = pt1[0]
            else:
                slp = (pt2[1] - pt1[1])/(pt2[0]-pt1[0])
                ctp = pt1[1] - slp*pt1[0]
            slps.append(slp)
            ints.append(ctp)

arr=np.array([slps,ints]).T

ulns = np.unique(np.round(arr,9),axis=0)

cnt =  0 

totlns = len(ulns)
chlst = map(int,totlns*np.linspace(0,1,100))

import pandas as pd

fqcnt = pd.Series(ulns[:,0]).value_counts().values


fval = len(ulns)**2-np.sum((fqcnt-1)*fqcnt) - len(ulns)

print fval

#print totlns

#print "start 2 "
#for i,ln in enumerate(ulns): 
#    if i in chlst:
#        print float(i)/totlns 
#    vls = np.abs(ulns[:,0]-ln[0])
#    intcnt = np.sum(vls < 0.000000001)-1 # lines with same slope
#    cnt = cnt + len(ulns) - 1 - intcnt

#print totlns
#print cnt




