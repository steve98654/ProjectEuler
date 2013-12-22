cnt = 0

for i in xrange(1,2**30+1):
    if(i^(2*i)^(3*i)==0):
        cnt = cnt + 1

print cnt

