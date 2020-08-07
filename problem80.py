#Problem 80: https://projecteuler.net/problem=80

from decimal import *

#Implementation of the Babylonian method for calculating square roots
#https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Babylonian_method

def sqrt(n:int):
    x0 = n / 2
    x1 = babylon(n, x0)
    for _ in range(10000):
        x1 = Decimal(babylon(n, x1))

    return x1

def babylon(n:int, x:int):
    return Decimal(0.5) * (Decimal(x) + Decimal(n) / Decimal(x))

#returns de sum of the first 100 digits of an number n
def sumOfDigit(n:int):
    sum = 0
    numb = str(n)
    for i in range(0, 101):
        if numb[i] == ".":
            continue
        digit = int(numb[i])
        sum = sum + digit
    return sum

if __name__ == '__main__':
    #set globall precission for the type Decimal
    getcontext().prec = 150
    sum = 0
    j = 1
    #sum up all sums of the first 100 digits for all numbers until 100 which have irrational square Methods_of_computing_square_roots
    for i in range(1, 100):
        if j*j == i:
            j = j +1
            continue
        else:
            sum = sum + sumOfDigit(sqrt(i))
    print("Solution: {}".format(sum))
