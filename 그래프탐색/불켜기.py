from collections import deque
from heapq import heappush, heappop
N, M = map(int, input().split())
dic = {}
dic2 = {}
for _ in range(M) :
    y1, x1, y2, x2 = map(int, input().split()) 
    dic[(y1, x1)] = dic.get((y1, x1), []) + [(y2, x2)]
result = 0
que = deque()
visited = [[0]*(N+1) for _ in range(N+1)]
visited2 = [[False]*(N+1) for _ in range(N+1)]

direct_y = [1,0,-1,0]
direct_x = [0,1,0,-1]
visited[1][1] = 1
que.append((1, 1, 1))

while que :
    level, y, x = que.popleft()
    for n_y, n_x in dic.get((y, x), []) :
        if visited[n_y][n_x] : continue
        visited[n_y][n_x] = level+1
        que.append((level+1, n_y, n_x))
# for a in visited :
#     print(*a)
dic2[(1, 1)] = 1
que2 = []
que.append((1, 1))
Max = 1
cnt = 0
while que :
    tmp = Max
    y, x = que.popleft()
    if visited2[y][x] : continue
    visited2[y][x] = True

    for n_y, n_x in dic.get((y, x), []) :
        dic2[(n_y, n_x)] = 1

    for i in range(4) :
        dy = direct_y[i] + y
        dx = direct_x[i] + x
        if dy < 1 or dx < 1 or dy > N or dx > N or visited[dy][dx] == 0: continue
        if visited2[dy][dx] : continue
        if visited[dy][dx] <= Max+1 :
            if Max < visited[dy][dx] :
                tmp = visited[dy][dx]
            que.append((dy, dx))
        else :
            heappush(que2, (visited[dy][dx], dy, dx))
    Max = tmp
    
    while que2 :
        level, n_y, n_x = heappop(que2)
        if level > Max+1 : 
            heappush(que2,(level, n_y, n_x))
            break
        else :
            if Max < level :
                Max = level
            que.append((n_y, n_x))
    
    visited[y][x] = 0
print(len(dic2))

