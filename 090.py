# Project Euler Problem 90
#! /usr/bin/python

from itertools import *
from numpy import *

cmbs = list(combinations(range(10),6)) # Make all possible combinations
ecmbs = map(list,cmbs)

for i in ecmbs:                        # Make extended lists
    if i.count(6) is 1 and i.count(9) is 0:
        i = i.append(9)
    elif i.count(9) is 1 and i.count(6) is 0:
        i = i.append(6)

# Define desired set of die values
tplst = set(["01","04", "09", "16", "25", "36", "49", "64", "81"])

# Form all 2-tuples from combinations and check to see if tplst is a subset.

cnt = 0
for k in ecmbs:
    for m in ecmbs:
        tpls1 = set(([str(i)+str(j) for i in k for j in m]))
        tpls2 = set(([str(j)+str(i) for i in k for j in m]))
        tpls = tpls1 | tpls2

        if len(tpls & tplst) == 9:
            cnt += 1 
    
print cnt/2 # Divide by two because we double counted
