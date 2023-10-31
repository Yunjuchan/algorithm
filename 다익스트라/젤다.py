import sys
from heapq import *
input = sys.stdin.readline
INF = 21e8
tc = 1
while True :

    N = int(input().rstrip())
    if N == 0 : break
    arr = [list(map(int, input().split())) for _ in range(N)]
    dist = [[INF]*N for _ in range(N)]
    direct_y = [1,0,-1,0]
    direct_x = [0,1,0,-1]

    que = []
    heappush(que, (arr[0][0], 0, 0))
    dist[0][0] = arr[0][0]

    while que :
        w, y, x = heappop(que)
        if y == x == N-1 : break
        if dist[y][x] < w : continue
        for i in range(4) :
            dy = direct_y[i] + y
            dx = direct_x[i] + x
            if dy < 0 or dx < 0 or dy >= N or dx >= N : continue
            if dist[dy][dx] > w + arr[dy][dx] :
                dist[dy][dx] = w + arr[dy][dx]
                heappush(que, (dist[dy][dx], dy, dx))
    print(f'Problem {tc}: {dist[N-1][N-1]}')
    tc += 1