#! usr/bin/env python

flst = []
flst.append(0)
flst.append(1)

for _ in xrange(100):
    flst.append(flst[-1]+flst[-2])

#print flst
llst = filter(lambda x: x < 10**17, flst)

print llst[-1]
print flst[-1]
