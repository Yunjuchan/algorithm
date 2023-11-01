## dp
import sys
input = sys.stdin.readline
N = int(input().rstrip())
arr = [list(map(int, input().split())) for _ in range(N)]
INF = 21e8
dp = [[INF]*(N+1) for _ in range(N+1)]
dp[1][1] = 0
direct_y = [0,-1]
direct_x = [-1,0]
for i in range(1, N+1) :
    for j in range(1, N+1) :
        for k in range(2) :
            dy = direct_y[k] + i
            dx = direct_x[k] + j
            if dx == 0 or dy == 0 : continue
            tmp = max(arr[i-1][j-1]-arr[dy-1][dx-1]+1, 0)
            if dp[i][j] > tmp + dp[dy][dx] :
                dp[i][j] = tmp + dp[dy][dx]
print(dp[N][N])

## 다익
import sys
from heapq import *
input = sys.stdin.readline
N = int(input().rstrip())
arr = [list(map(int, input().split())) for _ in range(N)]
INF = 21e8
dp = [[INF]*(N) for _ in range(N)]
dp[0][0] = 0
que = []
heappush(que, (0,0,0))
direct_y = [0,1]
direct_x = [1,0]
while que :
    w, y, x = heappop(que)
    if w > dp[y][x] : continue
    if y == x == N-1 : break
    for k in range(2) :
        dy = direct_y[k] + y
        dx = direct_x[k] + x
        if dx == N or dy == N : continue
        tmp = max(arr[dy][dx]-arr[y][x]+1, 0)
        if dp[dy][dx] > tmp + dp[y][x] :
            dp[dy][dx] = tmp + dp[y][x]
            heappush(que, (dp[dy][dx], dy, dx))
print(dp[N-1][N-1])

