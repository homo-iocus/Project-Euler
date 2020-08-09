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
