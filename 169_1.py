class Memoize:
    def __init__(self, f):
        self.f = f
        self.memo = {}
    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args] = self.f(*args)
        return self.memo[args]

@Memoize
def Val(n): 
    if(n == 0 or n == 1):
        return 1
    elif(n%2 == 0):
        return Val(n/2) + Val(n/2-1)
    else:
        return Val((n-1)/2)

print Val(10**25)

