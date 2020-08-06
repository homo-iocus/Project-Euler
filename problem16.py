#Problem 16: https://projecteuler.net/problem=16

#Funktion zur Quersummenberechnung
def CheckSum(n:int)-> int:
    sum = 0
    n = str(n)
    for literal in n:
        sum = sum + int(literal)
    return sum

print(CheckSum(2**1000))
