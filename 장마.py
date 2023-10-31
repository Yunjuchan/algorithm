from heapq import *
N, M = map(int, input().split())
INF = 21e8
arr = [list(map(int, input().split())) for _ in range(N)]
dist = [[INF]*M for _ in range(N)]

que = []
heappush(que, (arr[0][0], 0, 0))

dist[0][0] = arr[0][0]

direct_y = [-1,1,0,0]
direct_x = [0,0,-1,1]

while que :
    d, y, x = heappop(que)
    if y == N-1 and x == M-1 : break
    arr[y][x] = -1
    if dist[y][x] < d : continue

    for i in range(4) :
        dy = direct_y[i] + y
        dx = direct_x[i] + x
        if dy < 0 or dx < 0 or dy >= N or dx >= M : continue
        if arr[dy][dx] == -1 : continue
        tmp = arr[dy][dx] + d
        if dist[dy][dx] >  tmp :
            dist[dy][dx] = tmp
            heappush(que, (tmp, dy, dx))


if dist[N-1][M-1] == INF :
    print(-1)
else :
    print(dist[N-1][M-1])