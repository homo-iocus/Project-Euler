#Problem 40: https://projecteuler.net/problem=40

#generate Champernowne's constant until the 100001 digit
fraction = "0.1"
for i in range(2, 1000001):
    fraction= fraction + str(i)

#Calculate Solution and print it out

print(int(fraction[2]) * int(fraction[11])* int(fraction[101])*int(fraction[1001])* int(fraction[10001]) * int(fraction[1000001]) * int(fraction[100001]))
