#! /usr/bin/env python
# Project Euler Problem 225

def TriPer(m):
    a = 1; b = 1; c = 3 #// manually do one iteration
    n = 1
    while (a != 1 or b != 1 or c != 1):
        tmp = (a + b + c) % m
        if(tmp == 0):
            return 0
        a = b; b = c; c = tmp
        n += 1
    return n

oddmx = 2000
odd = [2*m+1 for m in xrange(1,oddmx)]

lst = []
for m in odd:
    if(TriPer(m)!=0):
        lst.append(m)

print lst[123]

