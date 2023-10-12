direct_y = [1,0,-1,0]
direct_x = [0,1,0,-1]
def dfs(y, x, level) :
    global Max 
    if level > Max :
        Max = level
    for i in range(4) :
        dy = direct_y[i] + y
        dx = direct_x[i] + x
        if dy < 0 or dy >= N or dx < 0 or dx >= N : continue
        if arr[dy][dx] < arr[y][x] :
            visited[dy][dx] = True
            dfs(dy, dx, level+1)
import sys
input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[1]*N for _ in range(N)]
visited = [[False] * N for _ in range(N)]

Max = 1
for i in range(N) :
    for j in range(N) :
        if visited[i][j] : continue
        visited[i][j] = True
        dfs(i, j, 1)
print(Max)