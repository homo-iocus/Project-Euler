#Problem 48: https://projecteuler.net/problem=48

sum = 0
for i in range(1, 1001):
    sum = sum + (i ** i)

#print last ten digits of the sum out
print(str(sum)[-10:])
