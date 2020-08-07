#Problem 22: https://projecteuler.net/problem=22

txt = open("Assets/names22.txt", "r")
sorted = txt.read().split("\",\"")
sorted[0] = 'MARY'

sorted.sort()
alpha = ["\"", "A" ,"B","C", "D", "E", "F", "G", "H", "I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W", "X", "Y","Z"]

sum = 0
for name in sorted:
    fact1 = sorted.index(name) + 1
    fact2 = 0
    for literal in name:
        fact2 = fact2 + alpha.index(literal)
    sum = sum + fact1 * fact2

print("Solution: {}".format(sum))
