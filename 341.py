def a(n):
    if n == 1: 
        return 1
    else: 
        return 1 + a(n - a(a(n-1)))

print a(10)
