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



ambicableNums = amicableNums(10000)
sum = 0
for el in ambicableNums:
    sum = sum + el
print(sum)
