#Problem 3 : https://projecteuler.net/problem=3

# solution from forum by seraph76

def factors(param):
    i = 2
    factors = []
    while i <= param:
        if (param % i) == 0:
            factors.append(i)
            param = param / i
        i += 1
    return factors



print(factors(600851475143))
