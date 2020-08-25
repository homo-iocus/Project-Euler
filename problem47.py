from Prime import trial_division

def numbOfPrimeFactor(li:list):
    safed:list = []
    count:int = 0
    for el in li:
        if el not in safed:
            safed.append(el)
            count += 1
        else:
            continue
    return count

for i in range(100000, 200000, 1):
    print("Checking for i = {}".format(i))
    if numbOfPrimeFactor(trial_division(i)) == 4 and numbOfPrimeFactor(trial_division(i+1)) == 4:
        if numbOfPrimeFactor(trial_division(i+2)) == 4 and numbOfPrimeFactor(trial_division(i+3)) == 4:
            print("Solution: {}".format(i))
            break
