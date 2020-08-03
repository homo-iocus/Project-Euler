#Problem 5: https://projecteuler.net/problem=5

def checkIfDivisibleUntil20(n):
    count = 0
    for i in range(1, 21):
        if n % i == 0:
            count = count + 1
        else:
            return False
            break
    if count == 20:
        return True


if __name__ == '__main__':
    for i in range(1, 1000000000):
        if checkIfDivisibleUntil20(i):
            print(i)
            break

#result = 232792560
