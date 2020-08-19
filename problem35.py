#Problem 35: https://projecteuler.net/problem=35

#Unnefficent but it works

from Prime import isPrime

#returns all circular numbers of an input number n
def circle(n:int):
    n = str(n)
    li = [int(n)]
    for i in range(1, len(n)):
        new_numb = n[i:] + n[:i]
        li.append(int(new_numb))
    return li



#checks for a list of numb if all are prime
def checkCircPrime(n:list)->bool:
    for nums in n:
        if not isPrime(nums):
            return False
    return True



count = 0
for i in range(1, 1000000):
    numbs = circle(i)
    if checkCircPrime(numbs):
        count = count + 1

print("Solution{}".format(count))
