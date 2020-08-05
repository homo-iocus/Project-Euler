
#Problem 9:  https://projecteuler.net/problem=9

def Tripple():
    for numb in range(500):
        a = numb
        for numb in range(500):
            b = numb
            for numb in range(500):
                c = numb
                if a < b < c:
                    if a**2 + b**2 == c**2:
                        if a + b + c == 1000:
                            return a*b*c
    return "Nothing Found"


print(Tripple())
