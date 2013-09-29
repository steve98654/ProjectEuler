from fractions import gcd

def factor(x):
    factors = []
    i = 2
    while x > 1:
        if x % i == 0:
            x = x / i
            factors.append(i)
        else:
            i += 1
    return factors

def prod(lst):
    tmp = 1;
    for x in lst:
        tmp*=x
    return tmp    

cmx = 120000
sm = 0

fcts = [0]

for i in xrange(1,cmx):
    fcts.append(factor(i))

gcdtb = [[gcd(a,b) for b in xrange(1,cmx)] for a in xrange(1,cmx)]

print "Fin tab"

for a in xrange(1,cmx-1):
    if a%100 == 0:
        print a
    for b in xrange(a+1,cmx-a):
        c = a+b
#        if(gcd(a,b)==1 and gcd(a,c)==1 and gcd(b,c)==1):
        if(gcdtb[a-1][b-1] == 1 and gcdtb[a-1][c-1]==1 and gcdtb[b-1][c-1]==1):
            flst = fcts[a] + fcts[b] + fcts[c]
            if(prod(list(set(flst))) < c):
                sm += c

print sm
print list(set(factor(36))), prod([3,4,5])
