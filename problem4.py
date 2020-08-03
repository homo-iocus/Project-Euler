#Problem 4 : https://projecteuler.net/problem=4

def checkIfPalindromNumb(n):
    original:str = str(n)
    reversed:str = original[::-1]
    if original == reversed:
        return True
    else:
        return False


l = [] #Lösungsmenge

#Finde alle Palindromnummern von einem Produkt aus zwei 3-stelligen Zahlen
for i in range(100, 1000):
    for j in range(100, 1000):
        if checkIfPalindromNumb(i * j):
            l.append(i * j)

#Max in der Lösungsmenge ist die Lösung
print("Lösung = {}".format(max(l)))
