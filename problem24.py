#Problem 24: https://projecteuler.net/problem=24
from Number import heap

#to slow O(n^2) :(
def bubbleSort(l:list):
    for _ in range(len(l)):
        for j in range(len(l)-1):
            if(l[j] > l[j+1]):
                tmp = l[j+1]
                l[j+1] = l[j]
                l[j] = tmp

#much better :)
def merge_sort(l:list):
    if len(l) <= 1: return l
    mid = len(l) // 2
    left= l[0:mid]
    right = l[mid:len(l)]
    left_list = merge_sort(left)
    right_list = merge_sort(right)
    return merge(left_list, right_list)

def merge(left:list, right:list):
    l = 0
    r = 0
    final = []
    while(l < len(left) and r < len(right)):
        if(left[l] < right[r]):
            final.append(left[l])
            l += 1
        else:
            final.append(right[r])
            r += 1
    if(l < len(left)):
        for el in left[l:]:
            final.append(el) 
    elif(r < len(right)):
        for el in right[r:]:
            final.append(el)
    return final

if __name__ == '__main__':
    permutations = heap(10, [0, 1, 2, 3, 4, 5 ,6 ,7, 8, 9])
    permutations_clean = []
    for perm in permutations:
        s = ""
        for digit in perm:
            s += str(digit)
        permutations_clean.append(int(s))
    sorted = merge_sort(permutations_clean)
    print(f"Solution: {sorted[999999]}")