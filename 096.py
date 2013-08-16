#!/usr/bin/env python

from numpy import *

# specify a su doku array, and a tuple ind    
def sqrtn(arr, ind):
    iv = ind[0]
    jv = ind[1]
    rtnarr = range(9)

    if(iv in range(0,3) and jv in range(0,3)):
        rtnarr = arr[0:3].T[0:3].T.flatten()
    elif(iv in range(0,3) and jv in range(3,6)):
        rtnarr = arr[0:3].T[3:6].T.flatten()
    elif(iv in range(0,3) and jv in range(6,9)):
        rtnarr = arr[0:3].T[6:9].T.flatten()
    elif(iv in range(3,6) and jv in range(0,3)):
        rtnarr = arr[3:6].T[0:3].T.flatten()
    elif(iv in range(3,6) and jv in range(3,6)):
        rtnarr = arr[3:6].T[3:6].T.flatten()
    elif(iv in range(3,6) and jv in range(6,9)):
        rtnarr = arr[3:6].T[6:9].T.flatten()
    elif(iv in range(6,9) and jv in range(0,3)):
        rtnarr = arr[6:9].T[0:3].T.flatten()
    elif(iv in range(6,9) and jv in range(3,6)):
        rtnarr = arr[6:9].T[3:6].T.flatten()
    elif(iv in range(6,9) and jv in range(6,9)):
        rtnarr = arr[6:9].T[6:9].T.flatten()
    else:
        print "Index is out of range!"
     
    return rtnarr 

# return row from array given an index 
def rwrtn(arr, rwind):
    return arr[rwind]

# return a col from an array given an index
def clrtn(arr, clind):
    return arr.T[clind]

# test su doku array 
tstarr = array([[0,0,3,0,2,0,6,0,0],[9,0,0,3,0,5,0,0,1],[0,0,1,8,0,6,4,0,0],
                [0,0,8,1,0,2,9,0,0],[7,0,0,0,0,0,0,0,8],[0,0,6,7,0,8,2,0,0],
                [0,0,2,6,0,9,5,0,0],[8,0,0,2,0,3,0,0,9],[0,0,5,0,1,0,3,0,0]])

# test array solution
tstsol = array([[4,8,3,9,2,1,6,5,7],[9,6,7,3,4,5,8,2,1],[2,5,1,8,7,6,4,9,3],
                [7,2,9,5,6,4,1,3,8],[1,3,6,7,9,8,2,4,5],[3,7,2,6,8,9,5,1,4],
                [3,7,2,6,8,9,5,1,4],[8,1,4,2,5,3,7,6,9],[6,9,5,4,1,7,3,8,2]])

###############################

tmparr = tstarr

# find row or col with least number of zeros
rzro = array([sum(tmparr[i][:]==0) for i in range(0,9)])
czro = array([sum(tmparr.T[i][:]==0) for i in range(0,9)])

mnvl = min(concatenate((rzro,czro)))
ind1 = where(rzro == mnvl)
ind2 = where(czro == mnvl)

if len(ind1[0]) == 0: 
    tpind = [0,ind2[0][0]]
    tpind[0] = where(tmparr.T[:][ind2[0][0]] == 0)[0][0]
else: 
    tpind = [ind1[0][0],0]
    tpind[1] = where(tmparr[ind1[0][0]][:] == 0)[0][0]


trw = set(rwrtn(tmparr,tpind[0]))
tcl = set(clrtn(tmparr,tpind[1]))
tsq = set(sqrtn(tmparr,tpind))

tpnms = set(list(trw.union(tcl).union(tsq))[1:])
dset = list(set(range(1,10)).difference(tpnms))  # this is the difference set.

if len(dset) == 1:
    tmparr[tpind[0]][tpind[1]] = list(dset)[0]

## MAKE A LIST OF ALL CANDIDATE INDICIES AND IF THE ABOVE LENGTH CONDITION 
## DOES NOT HOLD, THEN GO TO NEXT CANDIDATE INDEX 
