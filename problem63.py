#Problem 63: https://projecteuler.net/problem=63

count = 0
for i in range(1, 100):
    for j in range(1, 100):
        if len(str(i**j)) == j:
            count += 1

print("Solution: {}".format(count))
