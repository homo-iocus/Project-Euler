from Prime import getPrimes
import math

def isPrime(n, primes):
    if n <= 1:
        return False
    for prime in primes:
        if prime > math.sqrt(n):
            break
        else:
            if n % prime == 0:
                return False

    return True

def isSquare(n):
    sqrt = round(math.sqrt(n))
    if sqrt * sqrt == n:
        return True
    return False

if __name__ == '__main__':
    primes = getPrimes(10000)
    for i in range(3, 10000, 2):
        #check if i is a composite number
        if(isPrime(i, primes)):
            continue

        for prime in primes:
            if prime > i:
                print(f"Solution: {i}")
                break
            diff = i - prime
            remainder = diff / 2
            if(isSquare(remainder)):
                break
