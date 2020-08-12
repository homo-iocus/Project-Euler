#Problem 37: https://projecteuler.net/problem=37
from Prime import isPrime

#Function for returning list of possible truncatable numbers
def pieceOfNumb(n:str):
  new_numbers:list = []
  for i in range(len(n)):
    new_numb1 = n[i:]
    new_numb2 = n[:i]
    if not new_numb1 == "":
        new_numbers.append(new_numb1)
    if not new_numb2 == "":
        new_numbers.append(new_numb2)
  return new_numbers

#check if all numbers in a list are primes.
def isAllPrime(j:list):
    for numb in j:
      if not isPrime(int(numb)):
          return False
    return True

print(isPrime(0))

sum = 0
found = 0
for i  in range(10, 1000000):
    print("checking for {}".format(i))
    numbs = pieceOfNumb(str(i))
    if isAllPrime(numbs):
        sum = sum + i
        found = found + 1
    #if we have found 11 numbers we can exit the loop
    if found == 11:
        break

#Print Solution out

print("Solution: {}".format(sum))
