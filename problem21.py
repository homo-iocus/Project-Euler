#Problem 21: https://projecteuler.net/problem=21

#function d() as described in the problem
#returns the sum of all divisors of an Number n 
def d(n:int):
    l:list = []
    sum = 0
    f = 1
    while f < n:
        if n %f == 0:
            l.append(f)
        f = f + 1
    for el in l:
        sum = sum + el
    return sum

#generates all amicable Nums under the input n
def amicableNums(n: int):
    l:list = []
    for a in range(n):
        b = d(a)
        if a == d(b) and a != b:
            l.append(a)
            l.append(b)
    l = list(set(l))
    l.sort()
    return l

#generate all amicable Numbers under 10000
ambicableNums = amicableNums(10000)

#add all ambicable Numbers together and print the sum
sum = 0
for el in ambicableNums:
    sum = sum + el
print(sum)
