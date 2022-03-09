#Problem 15: https://projecteuler.net/problem=15

# Recursive solution takes to long for a 20 x 20 grid
def number_of_comb(x:int, y:int):
    if x == 0 and y > 0: return number_of_comb(x, y-1)
    if x  > 0 and y == 0: return number_of_comb(x-1, y)
    if x == 0 and y == 0: return 1
    return number_of_comb(x-1, y) + number_of_comb(x, y-1)

# Dynamic programing approach
def number_of_comb_dp(n):
    dp = [[-1 for _ in range(n+1)] for _ in range(n+1)]
    dp[0][0] = 0
    dp[1][0] = 1
    dp[0][1] = 1
    for x in range(n+1):
        for y in range(n+1):
            if(x == 0 and dp[x][y] == -1):
                dp[x][y] = dp[x][y-1]
            if(y == 0 and dp[x][y] == -1):
                dp[x][y] = dp[x-1][y]
            if dp[x][y] == -1:
                dp[x][y] = dp[x-1][y] + dp[x][y-1]
    return dp[n][n]


if __name__ == '__main__':
    print(f"Solution: {number_of_comb_dp(20)}")