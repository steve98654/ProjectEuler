import math

maxn = 1000000000000
n = 0
eps = 1e-8
lst = []

for x in xrange(2,12000):
    for y in xrange(1,a):
        z = 1
        n = 0
        while(n < maxn):
            n = x**3*y*z*z+y*y*z
            sq = math.sqrt(n)
            if(abs(sq - round(sq)) < eps):
                lst.append(n)
                break
            else:
                z += 1

flst = filter(lambda x: x < maxn, lst)
print flst                
print sum(set(flst))

