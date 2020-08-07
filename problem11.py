grid = open("Assets/grid11.txt", "r")
gridstr:list = grid.read().split("\n")
gridstr.remove('')

li = []

max = 0
#wraps grid in an usefull format
for row in gridstr:
    elements = row.split()
    li.append(elements)
    #do all adjacent number right/left direction of the grid
    for i in range(17):
        prod = int(elements[i]) * int(elements[i+1]) + int(elements[i+2]) + int(elements[i+ 3])
        if prod > max:
            max = prod

#do all adjacent number down/up direction of the grid
for i in range(17):
    for j in range(20):
        prod = int(li[i][j]) * int(li[i+1][j]) * int(li[i+2][j])* int(li[i+3][j])
        if prod > max:
            max = prod

#do all adjacent number left to right-diagonal direction of the grid
for i in range(17):
    for j in range(17):
        prod = int(li[i][j]) * int(li[i+1][j+1]) * int(li[i+2][j+2])* int(li[i+3][j+3])
        if prod > max:
            max = prod

#do all adjacent number right to left -diagonal direction of the grid
for i in range(17):
    for j in range(17):
        prod = int(li[i][j]) * int(li[i+1][j-1]) * int(li[i+2][j-2])* int(li[i+3][j-3])
        if prod > max:
            max = prod

print(max)
