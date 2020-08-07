#Problem 13:  https://projecteuler.net/problem=13

txt = open("Assets/numb13.txt", "r")

li = txt.read().split()
sum = 0
for numb in li:
  sum = sum + int(numb)


print(str(sum)[0:10])
