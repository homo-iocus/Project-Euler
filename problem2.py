#Problem 2: https://projecteuler.net/problem=2
last = 1
last2 = 2
sum = 2
while last2 < 3524578:
    next = last + last2
    if next % 2 == 0:
        sum = sum + next
    last = last2
    last2 = next

print(sum)
