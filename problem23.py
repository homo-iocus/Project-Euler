#Problem 23: https://projecteuler.net/problem=23
import math

#function for generating all abundant numbers until n:
def genAbundantNumbers(n:int):
    li :list = []
    for i in range(n):
        sum = 0
        for numb in findAllDivisors(i):
            sum = sum + numb
        if sum > i:
            li.append(i)
    return li
#function for finding all proper divisors of an number n:
def findAllDivisors(n):
    li = []
    f =1
    while f < n:
        if n%f == 0:
            li.append(f)
        f = f +1
    return li

if __name__ == '__main__':
    #list of all abundant numbers until 28123
    abundant:list = genAbundantNumbers(28123)
    sumOfAbundant:list = []
    sum = 0

    #Generates a list with all sums of the abundant numbers
    for x in abundant:
        for y in abundant:
            sumOfAbundant.append(x + y)

    #use set for faster finding the elements of sumOfAbundant
    sumOfAbundantSet = set(sumOfAbundant)

    #Check all numbers until 28123 if they can be displayed as the sum of two abundant numbers
    #(or if they are in the set of all sums of abundant Numbers which was generated before)
    #if not adding them up for the solution
    for i in range(28123):
        print("Checking {}".format(i))
        if i in sumOfAbundantSet:
            continue
        else:
            sum = sum + i



    print("Solution: {}".format(sum))
