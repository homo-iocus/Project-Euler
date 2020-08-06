#Problem 12:  https://projecteuler.net/problem=12

from Prime import trial_division
import math

def numbsOfDivisors(n:int)-> int:
    number_of_factors = 0
    for i in range(1, int(math.sqrt(n))):
        if n % i == 0:
            number_of_factors = number_of_factors + 2 #Add 2 for i and the result
        else:
            continue
    return number_of_factors

def generateTriangleNumbers(n:int) -> list:
  l:list = [0, 1]
  for numb in range(2, n +1):
    l.append(l[numb -1] + numb)
  return l


triangelNums= generateTriangleNumbers(10000000)

for i in range(10000000):
    numb = triangelNums[i]
    # factors = allFActorsOfNumb(numbs)
    divisors =  numbsOfDivisors(numb)
    if divisors > 500:
        print("Solution:{}".format(numb))
        break
    else:
        print("Nothing found for the {}th Triangel Number with {} divisors".format(i, divisors ))
