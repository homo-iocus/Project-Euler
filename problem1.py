#Problem 1: https://projecteuler.net/problem=1

sum = 0
for number in range(1000):
    print(number)
    if number % 3 == 0 or number % 5 == 0:
        sum = sum + number


print(sum)
