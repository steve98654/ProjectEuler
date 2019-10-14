
alllst = []
for i in range(1,9):
    lst = [2*n for n in range(1, 256) if 2**i % (2*n - 1) == 1]
    print lst

