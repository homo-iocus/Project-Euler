#Funktion zur Quersummenberechnung
def CheckSum(n:int) -> int:
    sum = 0
    n = str(n)
    for literal in n:
        sum = sum + int(literal)
    return sum

def ggT(a:int, b: int) -> int:
    while b != 0:
        h = a % b;
        a = b;
        b = h;
    return a

def fib(n: int) -> int:
    if n == 0:
        return n
    last = 0
    next = 1
    for _ in range(1, n):
        last, next = next, last+next
    return next

def findAllDivisors(n):
    li = []
    f =1
    while f < n:
        if n%f == 0:
            li.append(f)
        f = f +1
    return li

# Implementation of the Heap algorithm which produces all Permutations of an number
li = []
def heap(k:int, n:list):
    if k == 1:
        li.append(list(n))
    else:
        heap(k-1, n)
        for i in range(0, k-1):
            if k % 2 == 0:
                n[i], n[k-1] = n[k-1], n[i]
            else:
                n[0], n[k-1] = n[k-1], n[0]
            heap(k-1, n)
    return li
    
#function for checking if an number is a perfect cubic number
def is_perfect_cube(x):
    x = abs(x)
    return int(round(x ** (1. / 3))) ** 3 == x
