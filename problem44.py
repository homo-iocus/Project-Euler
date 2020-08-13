#Problem 44: https://projecteuler.net/problem=44

#generate pentagonal Numbers until n
def pentagonal(n:int)->list:
    li:list[int] = []
    for i in range(1, n+1):
        numb = i*(3*i-1)/2
        li.append(int(numb))
    return set(li)


pentagonalNumbs = pentagonal(10000)

for k in pentagonalNumbs:
    for j in pentagonalNumbs:
        #check if the difference and the sum of the pentagonal number j and k are themself
        #pentagonal
        if k-j in pentagonalNumbs and k+j in pentagonalNumbs:
            #print out the difference od k and j which is the Solution
            print("Solution:{}".format(k - j))
            break
        else:
            continue
