import cvxpy as cp
import numpy as np

# Problem data.
n = 10

# Construct the problem.
x = cp.Variable(n)

obj = cp.Minimize(cp.sum_entries([(x[i] - x[i-1])*cp.sqrt(1-x[i]**2) for i in range(1,n)]))
consts = [x[0] == -1, x[-1]==1]
consts = [x[i] > x[i-1] for i in range(1,n)]

prob = cp.Problem(objective, constraints)
        
