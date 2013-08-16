# Solution for project Euler 108 from Brian (near top of forums)

def nsols(n):
    return sum(1 for x in range(n+1, n*2+1) if ((n*x) % (x-n)==0))

f = 2*3*5*7*11*13*17
for i in xrange(f,f*19,f):
    if nsols(i)>=10000:
        print i
        break

print xrange(f,f*17,f)
