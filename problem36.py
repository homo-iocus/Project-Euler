#Problem 36: https://projecteuler.net/problem=36

#Function for checking if an string is palindrome
def isPalindrome(n:str):
  if n == n[::-1]:
    return True
  else:
    return False

sum = 0
for i in range(1000000):
  #check if numb in base 10 and base 2 is palindrom
  #if true add the numbers up
  if isPalindrome(str(i)) and isPalindrome(bin(i)[2:]):
    sum = sum + i

#Print Solution out
print("Solution: {}".format(sum))
