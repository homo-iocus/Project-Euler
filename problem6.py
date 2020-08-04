#Problem 6:  https://projecteuler.net/problem=5
sum1: int = 0
sum2:int  = 0
for i in range(1, 101):
    sum1 = sum1 + i
    sum2 = sum2 + i**2

square1: int = sum1**2

print("Lösung {}".format(square1 - sum2))
