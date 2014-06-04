from math import *
from time import *
import csv

#183544

t1 = time()

lim = 2*10**9
mx = int(ceil(sqrt(lim)))

print mx 

tb1 = [i*i + j*j for i in range(1,mx+1) for j in range(1,mx+1) if i*i+j*j < lim]

print len(tb1)

tb2 = [i*i + 2*j*j for i in range(1,mx+1) for j in range(1,mx+1) if i*i+j*j < lim]

print len(tb2)

tb3 = [i*i + 3*j*j for i in range(1,mx+1) for j in range(1,mx+1) if i*i+j*j < lim]

print len(tb3)

tb4 = [i*i + 7*j*j for i in range(1,mx+1) for j in range(1,mx+1) if i*i+j*j < lim]

print len(tb4)

t2 = time() 

tps1 = set.intersection(set(tb1),set(tb2),set(tb3),set(tb4))
tps2 = set.intersection(tps1, set(tb3))
lst  = set.intersection(tps2, set(tb4))

t3 = time()

print len(lst)
print t2 - t1
print t3 - t1

with open("229_1.csv", "wb") as f:
    wr = csv.writer(f)
    wr.writerow(list(lst))
