#Problem 52: https://projecteuler.net/problem=52

#Function for checking if two numbers consist of the same digits
def containsTheSameDigit(n:int, m:int)-> bool:
    n = str(n)
    m = str(m)
    for literal in n:
        if literal not in m:
            return False
    return True


#serach x 
for x in range(1,1000000):
    x2 = x * 2
    x3 = x * 3
    x4 = x * 4
    x5 = x * 5
    x6 = x * 6
    if containsTheSameDigit(x, x2) and containsTheSameDigit(x2, x3):
        if containsTheSameDigit(x3, x4) and containsTheSameDigit(x5, x4):
            if containsTheSameDigit(x6, x):
                print("Solution: {}".format(x))
                break
