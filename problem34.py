#Problem 34: https://projecteuler.net/problem=34

import math

special_numb: list = [] #empty list for storing the special numbers

for i in range(3, 100000):
    string = str(i)
    factorial_sum = 0
    #sum th factorial of the digit of an number up
    for literal in string:
        factorial_sum = factorial_sum + math.factorial(int(literal))
    #if the sum of the factorials is equal to the number itself append the
    #number in the special numb list
    if factorial_sum == i:
        special_numb.append(i)

sum = 0
#iterate trough the special numb list and adding all numbers up
for numb in special_numb:
    sum = sum + numb

print("solution: {}".format(sum))
