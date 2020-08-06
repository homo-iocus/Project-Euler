import math
#Implementation of the Sieve of Eratosthenes for finding all Primes until the input number

def getPrimes(n:int):

    primes: list[int] = []
    gestrichen : list[bool] = [True, True]
    for i in range(2, n):
        gestrichen.append(False)

    for i in range(2, int(math.sqrt(n))):
       if not gestrichen[i]:

           primes.append(i)
           for j in range(i**2, n, i):

               gestrichen[j] = True


    for i in range(int(math.sqrt(n)) + 1, n):

        if not gestrichen[i]:

            primes.append(i)
    return primes

def isPrime(n:int):
    primes:list[int] = getPrimes(1000)
    for prime in primes:
        if prime > math.sqrt(n):
            break
        else:
            if n % prime == 0:
                return False

    return True
#Primfaktorzerlegung 
def trial_division(n: int) -> list:
    # Return a list of the prime factors for a natural number.
    a = []               # Prepare an empty list.
    f = 2                # The first possible factor.
    while n > 1:         # While n still has remaining factors...
        if n % f == 0:   # The remainder of n divided by f might be zero.
            a.append(f)  # If so, it divides n. Add f to the list.
            n /= f       # Divide that factor out of n.
        else:            # But if f is not a factor of n,
            f = f + 1       # Add one to f and try again.
    return a             # Prime factors may be repeated: 12 factors to
