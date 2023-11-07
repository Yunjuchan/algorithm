direct_y = [1,0,-1,0]
direct_x = [0,1,0,-1]

def dfs(y, x) :
    if dp[y][x] != 1 :
        return dp[y][x]
    for i in range(4) :
        dy = direct_y[i] + y
        dx = direct_x[i] + x
        if dy < 0 or dy >= N or dx < 0 or dx >= N : continue

        if arr[dy][dx] > arr[y][x] :
            ret = dfs(dy, dx)
            dp[y][x] = max(dp[y][x], ret+1)

    return dp[y][x]
        
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N = int(input().rstrip())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[1]*N for _ in range(N)]

Max = 1
for i in range(N) :
    for j in range(N) :
        if dp[i][j] != 1 : continue
        dfs(i, j)
        if Max < dp[i][j] :
            Max = dp[i][j]
print(Max)