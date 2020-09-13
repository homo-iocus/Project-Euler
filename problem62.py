#Problem 62: https://projecteuler.net/problem=62
#Runtimeof this script : ~ 305,532s 

#function for checking if two numbers a and b are permutations of one and another
def isPermutation(a:int, b:int):
    count = [0,0,0,0,0,0,0,0,0,0]
    for digit1 in str(a):
        count[int(digit1)] += 1
    for digit2 in str(b):
        count[int(digit2)] -= 1

    for i in count:
        if i != 0:
            return False
    return True

#function for generating cubic numbers
def genCubicNumbers(k:int, n:int)->list:
    listee = list()
    for i in range(k, n):
        listee.append(i**3)
    return listee

if __name__ == '__main__':
    cubicNumbers = genCubicNumbers(1000, 10000)
    for cube1 in cubicNumbers:
        count = 0
        for cube2 in cubicNumbers:
            if isPermutation(cube1, cube2):
                count += 1
            else:
                continue
        if count == 5:
            print("Solution: {}".format(cube1))
            break
