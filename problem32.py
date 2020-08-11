def isPanadigital(n:str):
    if len(n) > 9:
        return False
    for i in range(1, 10):
        if str(i) not in n:
            return False
    return True


if __name__ == '__main__':
    products: list = []
    for i in range(10000):
        for j in range(10000):
            product = j * i
            string = str(product) + str(i) + str(j)
            if isPanadigital(string):
                if product not in products:
                    products.append(product)

            else:
                continue
    sum = 0
    for el in products:
        sum = sum + el


    print("Solution: {}".format(sum))
