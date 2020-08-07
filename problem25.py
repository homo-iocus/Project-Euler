#Problem 25: https://projecteuler.net/problem=25
def fib(n: int) -> int:
    if n == 0:
        return n
    last = 0
    next = 1
    for _ in range(1, n):
        last, next = next, last+next
    return next


if __name__ == '__main__':
    l =[]
    #generate the first 10thousand fibannoci numbers
    for i in range(10000):
        fiba = fib(i)
        l.append(fiba)
    # print(l)

    #check fibannoci numbers for there length until one is 1000 digit long

    for numb in l:
        if len(str(numb)) == 1000:
            print(l.index(numb))
            break
