#Problem 56: https://projecteuler.net/problem=56

#function to find the sum of all digits of an number
def sumOfDigit(n:int):
    n = str(n)
    sum = 0
    for digit in n:
        sum = sum + int(digit)
    return sum


max = 0
for a in range(1, 100):
    for b in range(1, 100):
        num = a **b
        sum = sumOfDigit(num)
        if sum > max:
            max = sum


print("Solution:{}".format(max))
