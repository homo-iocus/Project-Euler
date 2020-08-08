#Problem 30: https://projecteuler.net/problem=30

li = [] #empty list for storing can be written as the sum of fifth powers of their digits

#generate numbers which can be written as the sum of fifth powers of their digits
for i in range(2, 1000000):
    sum = 0
    for literal in str(i):
        sum = sum + int(literal)**5
    if sum == i:
        li.append(i)

solution = 0
#add founded numbers up
for element in li:
    solution = solution + element
print("Solution: {}".format(solution))
