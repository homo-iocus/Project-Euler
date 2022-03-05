#Problem 60: https://projecteuler.net/problem=60ƒ
from Prime import getPrimes
import math

primes: list = getPrimes(10000)
print(f"Number of primes to check:{len(primes)}")

def checkIfProducePrime(n: int, m: int) -> bool:
    new_numb = int(str(n) + str(m))
    new_numb2 = int(str(m) + str(n))
    if isPrime(new_numb, primes) and isPrime(new_numb2, primes):
        return True
    else:
        return False




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


def run():
    li = []
    for prime1 in primes:
        for prime2 in primes:
            if checkIfProducePrime(prime1, prime2):
                for prime3 in primes:
                    if checkIfProducePrime(prime1, prime3) and checkIfProducePrime(prime2, prime3):
                        for prime4 in primes:
                            if checkIfProducePrime(prime4, prime1) and checkIfProducePrime(prime4, prime2):
                                if checkIfProducePrime(prime4, prime3):
                                    for prime5 in primes:
                                        if checkIfProducePrime(prime5, prime1) and checkIfProducePrime(prime5, prime2):
                                            if checkIfProducePrime(prime5, prime3) and checkIfProducePrime(prime5, prime4):
                                                li.append(prime1)
                                                li.append(prime2)
                                                li.append(prime3)
                                                li.append(prime4)
                                                li.append(prime5)
                                                return li


list = run()
print("ended run function")
sum = 0
if(not list):
    print("No solution found")
else:
    for el in list:
        sum = sum + el

    print("Solution: {}".format(sum))
