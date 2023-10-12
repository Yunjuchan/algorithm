from heapq import heappop, heappush
direct_y = [1,0,-1,0]
direct_x = [0,1,0,-1]
T = int(input())
for tc in range(1, T+1) :
    N, M = map(int, input().split())
    INF = 21e8
    arr = [list(map(int, input().split())) for _ in range(N)]
    dist = [[INF] * N  for _ in range(N)]
    adj = {}
    for i in range(N) : 
        for j in range(N) :
            for k in range(4) :
                dy = direct_y[k] + i
                dx = direct_x[k] + j
                if dy < 0 or dx < 0 or dy >= N or dx >= N : continue
                adj[(i,j)] = adj.get((i,j), []) + [[dy, dx, -1]]

    for _ in range(M) :
        y1, x1, y2, x2, a = map(int, input().split())
        adj[(y1-1, x1-1)].append([y2-1, x2-1, a]) 
        adj[(y2-1, x2-1)].append([y1-1, x1-1, a])
    que = []
    heappush(que, [0, 0, 0])
    while que :
        y, x, d = heappop(que)
        if y == x == N-1 : break
        for dy, dx, a in adj[(y, x)] :
            if a == -1 :
                if arr[dy][dx] > arr[y][x] :
                    tmp = (arr[dy][dx] - arr[y][x])*2
                elif arr[dy][dx] < arr[y][x] :
                    tmp = 0
                else :
                    tmp = 1  
                if dist[dy][dx] > d + tmp :
                    dist[dy][dx] = d + tmp
                    heappush(que, [dy, dx, dist[dy][dx]])
            else :
                if dist[dy][dx] > d + a :
                    dist[dy][dx] = d + a
                    heappush(que, [dy, dx, dist[dy][dx]])
    print(f'#{tc} {d}')
