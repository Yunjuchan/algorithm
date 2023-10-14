import sys
from heapq import heappush, heappop
input = sys.stdin.readline
direct_y = [1,0,-1,0]
direct_x = [0,1,0,-1]
N, M = map(int, input().split())
arr = [input() for _ in range(N)]
que = []
INF = 21e8
visited = [[[INF]*M for _ in range(N)] for _ in range(2)]
visited[0][0][0] = visited[1][0][0] = 1
heappush(que, (0, 1, 0, 0))
while que :
    tp, cnt, y, x = heappop(que)
    for i in range(4) :
        dy = direct_y[i] + y
        dx = direct_x[i] + x
        if dy < 0 or dx < 0 or dy >= N or dx >= M : continue
        if arr[dy][dx] == '0' :
            if visited[tp][dy][dx] <= cnt+1 : continue
            visited[tp][dy][dx] = cnt+1
            heappush(que, (tp, cnt+1, dy, dx))
        elif tp == 0 :
            if visited[1][dy][dx] <= cnt+1 : continue
            visited[1][dy][dx] = cnt+1
            heappush(que, (1, cnt+1, dy, dx))
result = min(visited[0][N-1][M-1], visited[1][N-1][M-1])

if result == INF :
    print(-1)
else :
    print(result)