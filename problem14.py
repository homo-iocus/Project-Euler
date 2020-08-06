#Problem 14: https://projecteuler.net/problem=14

from loadingBar import printProgressBar
li:list= []                 #list to temporary store a Collatz Sequenze
max_length = 0

def CollatzSeq(n:int):
    li.append(n)
    if n == 1:
        return "Generated"
    if n % 2 == 0:          #check if n is even or odd
        CollatzSeq(n / 2)
    else:
        CollatzSeq(n * 3 + 1)


for i in range(2, 1000000):
    CollatzSeq(i)
    if len(li) > max_length:
        max_length = len(li)
        solution = i
    li.clear()              #empty the list for the next iteration

print("Solution{}".format(solution))
