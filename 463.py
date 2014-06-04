def f(n):
    if n == 1:
        return 1
    elif n == 3:
        return 3
    elif n%2 == 0:
        return f(n/2)
    elif n%4 == 1:
        return 2*f(2*(n-1)/4+1) - f((n-1)/4)
    else: 
        return 3*f(2*((n-3)/4)+1) - 2*f((n-3)/4)

arrend = 100
arr = [f(n) for n in xrange(1,arrend+1)]
print sum(arr)
print arr
