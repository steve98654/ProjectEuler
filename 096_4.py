#!/usr/bin/env python

# This is not solving the more difficult puzzles.  Try another approach.
# BUILD IN GUESSING IF MAXITER IS REACHED

from numpy import *
import copy

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
    tstinds = [[0,0],k[3,0],[6,0],[3,0],[3,3],[3,6],[6,0],[6,3],[6,6]]
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
    
        # START HERE!!
        # build logic in here.  if wcntmx == cntmx - 1, 
        # save current state
        # guess for index with fewest numbers and try to solve
        # if we cannot get a solution, then try other candidates

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

# return the possible values of a zero in an array
def posvals(tmparr, ind): 
    
    tpind = ind
    trw = set(rwrtn(tmparr,tpind[0]))
    tcl = set(clrtn(tmparr,tpind[1]))
    tsq = set(sqrtn(tmparr,tpind))
    tpnms = set(list(trw.union(tcl).union(tsq))[1:]) # numbers in row, col, or sqr    
    dset = list(set(range(1,10)).difference(tpnms))  # this is the difference set.
    
    return dset

## Let's build a separate guessing function instead.

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
numpuz = 2 # number of puzzles to solve from file

for k in range(numpuz): 
    tpuz = content[10*k+1:10*(k+1)]

    tarr = zeros((9,9))

    for i in range(9):
        for j in range(9):
            tarr[i][j] = int(tpuz[i][j])

    ## main solver call.  If there are zeros left, then run it into the guessing function
    outarr = solver(tarr)

    ## This is the crux of a single guess method (single guess) if main solver does not work
    if len(zroind(outarr)) > 0:
        print "There are %r zeros left" % len(zroind(outarr))
        guessarr = copy.deepcopy(outarr)  # save copy of out array
        guessinds = zroind(guessarr) # find indicief of zeros 
        pvls = [posvals(outarr,ind) for ind in guessinds] # find possible values for zeros
        pvllen = map(len,pvls)  # find lengths of possibilities 
        minvlinds = [i for i, x in enumerate(pvllen) if x == min(pvllen)] # min len indexes
        
        cndinds = [guessinds[i] for i in minvlinds] # candidate min inds 
        cndvals = [pvls[i] for i in minvlinds] # candidate min inds 

        # code for testing purposes 
        cndinds = guessinds
        cndvals = pvls

        for k2 in range(len(cndinds)):
            for k3 in range(len(cndvals[k2])):
                guessarr[cndinds[k2][0]][cndinds[k][1]] = cndvals[k2][0]  # make the guess
                solver(guessarr)
                if len(zroind(guessarr)) == 0:
                    break
                    print "GOT IT!!!!!!!!!!!!!" 
                else:
                    print guessarr
                    guessarr = copy.deepcopy(outarr)
            if len(zroind(guessarr)) == 0:
                break
        ## FIND IND WITH MIN NUMBER OF POSSIBILITIES AND RETURN ALL GUESSES
        ## SUB IN GUESSES, THEN TRY TO SOLVE.   

    tparr = map(repr,map(int,outarr[0][0:3].tolist()))
    cnt += int("".join(tparr))
