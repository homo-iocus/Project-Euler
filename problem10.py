#Problem 10:  https://projecteuler.net/problem=10

from Prime import getPrimes
#All Primes below 2 Million
primes= getPrimes(2000000)

sum = 0
for prime in primes:
    sum = sum + prime

print(sum)
