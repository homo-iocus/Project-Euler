#Problem 53: https://projecteuler.net/problem=53

import math

def nCr(n:int, r:int)->int:
    return math.factorial(n) / (math.factorial(r) *math.factorial(n-r))


sum = 0
for n in range(1, 101):
    for r in range(1, n):
        numb = nCr(n, r)
        if numb > 1000000:
            sum = sum + 1


print("Solution: {}".format(sum))
