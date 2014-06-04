
nmx = 10**5
lst = []

for n in xrange(1,nmx+1):
    a = n
    while a*a%n != a:
        a -= 1
    lst.append(a)

print sum(lst)
