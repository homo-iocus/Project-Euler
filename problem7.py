#Problem 7:  https://projecteuler.net/problem=7

from Prime import getPrimes

primes = getPrimes(1000000)
print("Primzahlen: {}".format(primes))
print("ANz Primzahlen = {}".format(len(primes)))
print("Solution: {}".format(primes[10000]))
