#Funktion zur Quersummenberechnung
def CheckSum(n:int) -> int:
    sum = 0
    n = str(n)
    for literal in n:
        sum = sum + int(literal)
    return sum

def ggT(a:int, b: int) -> int:
    while b != 0:
        h = a % b;
        a = b;
        b = h;
    return a
