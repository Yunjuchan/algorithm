import sys
from collections import deque
input = sys.stdin.readline
direct_y = [1,0,-1,0]
direct_x = [0,1,0,-1]
N, M, K = map(int, input().split())
arr = [input() for _ in range(N)]
que = deque()
INF = 21e8
visited = [[[INF]*(K+1) for _ in range(M)] for _ in range(N)]
visited[0][0][K] = 1
que.append((K, 0, 0))
while que :
    tp, y, x = que.popleft()
    if y == N-1 and x == M-1 :
        print(visited[y][x][tp])
        break
    for i in range(4) :
        dy = direct_y[i] + y
        dx = direct_x[i] + x
        if dy < 0 or dx < 0 or dy >= N or dx >= M : continue
        if arr[dy][dx] == '0' :
            if visited[dy][dx][tp] <= visited[y][x][tp]+1 : continue
            visited[dy][dx][tp] = visited[y][x][tp] + 1
            que.append((tp, dy, dx))
        elif tp != 0 :
            if visited[dy][dx][tp-1] <= visited[y][x][tp]+1 : continue
            visited[dy][dx][tp-1] = visited[y][x][tp] + 1
            que.append((tp-1, dy, dx))
else :
    print(-1)
