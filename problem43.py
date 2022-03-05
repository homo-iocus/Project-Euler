#Problem 43: https://projecteuler.net/problem=43

from Number import heap
from Prime import getPrimes

def checkDivisibility(number:str, primes:list[int]):
    for i in range(7):
        numb = int(number[i+1:i+4])
        if(numb % primes[i] != 0):
            return False
    return True

if __name__ == '__main__':
    permutations = heap(10, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    primes = getPrimes(18)
    pandigits = []
    sum = 0
    for permu in permutations:
        s = ""
        for digit in permu:
            s += str(digit)
        pandigits.append(s)

    for number in pandigits:
        n = int(number)
        if(checkDivisibility(number, primes)):
            sum += n
    print(f"Solution : {sum}")