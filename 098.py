# Project Euler problem 98.

import csv
import re
import numpy
import itertools
import string

# Check if two strings are anagrams
def isAna(st1, st2):
    return (sorted(st1) == sorted(st2))

# Read in data
dat = []

with open('words2.txt','rb') as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        dat.append(row)

# Find commas in data
dat = str(dat)
cms = []

p = re.compile(",")
for m in p.finditer(dat):
    cms.append(m.start())
    #print m.start(), m.group()

# Build a list of words
words = ['A'] # build a list of words

for i in xrange(0,len(cms)-1):
     words.append(str(dat[cms[i]+3:cms[i+1]-1]))

awords = numpy.array(words)
alens  = map(len,awords)

# Sort words by size
atb = [] # atb[i][j] is jth word with length i 

for i in xrange(0,max(alens)):
    tpr = []
    for j in xrange(0,len(awords)): 
        if alens[j]==i:
            tpr.append(awords[j])
    atb.append(tpr)

# Find anagram pairs and store them in angwrd
angwrd = []

for k in xrange(1,len(atb)):
    tplst = atb[k][:]
    for i in tplst:
        for j in tplst:
            if i!=j and isAna(i,j) is True:
                angwrd.append([i,j])

# Remove duplicates pairs
tpres = map(sorted,angwrd)
tpres.sort()
flst = tpres[1::2]

# Substitute values into flst
eps = 1e-10
mxsqr = []

for k in xrange(1,len(flst)):
    # find unique chrs
    tpchrs = list(set([flst[k][0][x] for x in xrange(0,len(flst[k][0]))]))  

    #list of all possible permutations of letters
    pms = list(itertools.permutations(xrange(0,10),len(tpchrs)))
    print k,flst[k]

    for j in xrange(0,len(pms)):
        flstp1 = flst[k][0]
        flstp2 = flst[k][1]
        for i in xrange(0,len(pms[0])):
            flstp1 = str(flstp1).replace(tpchrs[i],str(pms[j][i]))
            flstp2 = str(flstp2).replace(tpchrs[i],str(pms[j][i]))
        if (int(flstp1[0]) is not 0) and (int(flstp2[0]) is not 0):
            sq1 = numpy.sqrt(float(flstp1))
            sq2 = numpy.sqrt(float(flstp2))
            tst1 = numpy.abs(sq1-numpy.round(sq1))
            tst2 = numpy.abs(sq2-numpy.round(sq2))
            if (tst1 < eps) and (tst2 < eps):
                mxsqr.append(max(int(flstp1),int(flstp2)))
# DEBUG LINE    print max(int(flstp1),int(flstp2)), flstp1, flstp2 

print "Max Square is %r" %(max(mxsqr))

