from collections import deque
import sys
input = sys.stdin.readline
K = int(input().rstrip())
W, H = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(H)]
arr2 = [[[0]*W for _ in range(H)] for _ in range(K+1)]
for i in range(K+1) :
    for j in range(H) :
        for k in range(W) :
            if arr[j][k] : arr2[i][j][k] = -1
            else : arr2[i][j][k] = 21e8

que = deque()
direct_y = [1,0,-1,0]
direct_x = [0,1,0,-1]
direct_y2 = [2,2,-2,-2,1,1,-1,-1]
direct_x2 = [1,-1,1,-1,2,-2,2,-2]
arr2[0][0][0] = 0
que.append((0,0,0))

while que :
    n, y, x = que.popleft()
    if y == H-1 and x == W-1 :
        break
    for i in range(4) :
        dy = direct_y[i] + y
        dx = direct_x[i] + x
        if dy < 0 or dx < 0 or dy >= H or dx >= W : continue
        if arr2[n][dy][dx] == -1 : continue
        if arr2[n][dy][dx] > arr2[n][y][x]+1 :
            arr2[n][dy][dx] = arr2[n][y][x]+1
            que.append((n, dy, dx))
    if n == K : continue
    for i in range(8) :
        dy = direct_y2[i] + y
        dx = direct_x2[i] + x     
        if dy < 0 or dx < 0 or dy >= H or dx >= W : continue
        if arr2[n+1][dy][dx] == -1 : continue
        if arr2[n+1][dy][dx] > arr2[n][y][x]+1 :
            arr2[n+1][dy][dx] = arr2[n][y][x]+1
            que.append((n+1, dy, dx))

Min = 21e8
for i in range(K+1) :
    if Min > arr2[i][H-1][W-1] :
        Min = arr2[i][H-1][W-1]
if Min == 21e8 :
    print(-1)
else :
    print(Min)