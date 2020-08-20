#Problem 29: https://projecteuler.net/problem=29

li=[]
for a in range(2, 101):
    for b in range(2, 101):
        number = a**b
        if number not in li:
            li.append(number)

print(len(li))
