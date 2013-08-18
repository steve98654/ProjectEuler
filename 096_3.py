#!/usr/bin/env python

# This is not solving the more difficult puzzles.  Try another approach.
# BUILD IN GUESSING IF MAXITER IS REACHED

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

# takes array as input and returns list of zero indicies
def zroind(arr):
    rtnind = []
    for i in range(9):
        for j in range(9):
            if(arr[i][j] == 0):
                rtnind.append([i,j])
    return rtnind

# returns 1 if solved and 0 if not solved
def soltst(arr):
    rwtst = [len(set(range(1,10)).difference(set(tstsol[i]))) for i in range(9)] 
    cltst = [len(set(range(1,10)).difference(set(tstsol.T[i]))) for i in range(9)]
    tstinds = [[0,0],[3,0],[6,0],[3,0],[3,3],[3,6],[6,0],[6,3],[6,6]]
    sqtst = [len(set(range(1,10)).difference(set(sqrtn(arr,ind).flatten()))) for ind in tstinds]
    
    sol = 0
    if max(rwtst) == 0 and max(cltst) == 0 and max(sqtst) == 0:
        sol=1
    return sol    

# main solver, takes numpy array as input, returns solved puzzle
def solver(tmparr): 

    tpinds = zroind(tmparr)
    wcnt = 0;
    wcntmx = 200

    while len(tpinds)>0 and wcnt < wcntmx:
    
        tpinds = zroind(tmparr)
    
        for i in range(len(tpinds)):
            tpind = tpinds[i]
    
            trw = set(rwrtn(tmparr,tpind[0]))
            tcl = set(clrtn(tmparr,tpind[1]))
            tsq = set(sqrtn(tmparr,tpind))
            tpnms = set(list(trw.union(tcl).union(tsq))[1:]) # numbers in row, col, or sqr
    
            dset = list(set(range(1,10)).difference(tpnms))  # this is the difference set.
            #print dset, len(dset)
            if len(dset) == 1:
                #print tmparr[tpind[0]][tpind[1]]
                tmparr[tpind[0]][tpind[1]] = dset[0]
        
        wcnt +=1        
    return tmparr                
                

# test su doku array 
tstarr = array([[0,0,3,0,2,0,6,0,0],[9,0,0,3,0,5,0,0,1],[0,0,1,8,0,6,4,0,0],
                [0,0,8,1,0,2,9,0,0],[7,0,0,0,0,0,0,0,8],[0,0,6,7,0,8,2,0,0],
                [0,0,2,6,0,9,5,0,0],[8,0,0,2,0,3,0,0,9],[0,0,5,0,1,0,3,0,0]])

# test array solution
tstsol = array([[4,8,3,9,2,1,6,5,7],[9,6,7,3,4,5,8,2,1],[2,5,1,8,7,6,4,9,3],
                [5,4,8,1,3,2,9,7,6],[7,2,9,5,6,4,1,3,8],[1,3,6,7,9,8,2,4,5],
                [3,7,2,6,8,9,5,1,4],[8,1,4,2,5,3,7,6,9],[6,9,5,4,1,7,3,8,2]])

###############################

# Now import and format different arrays and solve them 1 by 1.
# read in first puzzle, solve, save top three corners. 

with open('sudoku.txt','r') as f:
    content = f.readlines()

cnt = 0    

for k in range(2): 
    tpuz = content[10*k+1:10*(k+1)]

    tarr = zeros((9,9))

    for i in range(9):
        for j in range(9):
            tarr[i][j] = int(tpuz[i][j])

    outarr = solver(tarr)

    tparr = map(repr,map(int,outarr[0][0:3].tolist()))
    cnt += int("".join(tparr))
    print outarr

