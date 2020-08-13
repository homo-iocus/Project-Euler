#Problem 45: https://projecteuler.net/problem=45

#generate pentagonal Numbers until n
def pentagonal(n:int)->list:
    li:list[int] = []
    for i in range(1, n+1):
        numb = i*(3*i-1)/2
        li.append(int(numb))
    return set(li)

#generate triangle Numbers until n

def triangle(n:int)->set:
    li:list[int] = []
    for i in range(1, n+1):
        numb = i*(i+1)/2
        li.append(int(numb))
    return set(li)

#generate hexagonal Numbers until n

def hexagonal(n:int)->set:
    li:list[int] = []
    for i in range(1, n+1):
        numb = i*(2*i-1)
        li.append(int(numb))
    return set(li)

triangleNumbs = triangle(1000000)
pentagonalNumbs = pentagonal(1000000)
hexagonalNumbs = hexagonal(1000000)

#inform the waiting user that all numbs are generated
print("generated all numbs")

#check every triangle number if she is hexa- and pentagonal
for numb in triangleNumbs:
    if numb in pentagonalNumbs and numb in hexagonalNumbs:
        #filter out 1 and 40755
        if numb == 40755 or numb == 1:
            continue
        else:
            print("Solution: {}".format(numb))
            break
