import math
#Implementation of the Sieve of Eratosthenes for finding all Primes until the input number

def getPrimes(n:int):

    primes: list[int] = []
    gestrichen : list[bool] = [True, True]
    for i in range(2, n):
        gestrichen.append(False)


    print(len(gestrichen))
    for i in range(2, int(math.sqrt(n))):
       if not gestrichen[i]:

           primes.append(i)
           for j in range(i**2, n, i):

               gestrichen[j] = True


    for i in range(int(math.sqrt(n)) + 1, n):

        if not gestrichen[i]:

            primes.append(i)
    return primes
