def PyTripSml(max):
    lst = [];
    for m in xrange(1,max):
        for n in xrange(1,m):
            lst.append(m*m-n*n)
            lst.append(2*m*n)
    return lst

trp = PyTripSml(1000)

cnt = []
cntmx = 10000

for i in xrange(cntmx):
    cnt.append(trp.count(i))

print max(cnt)

