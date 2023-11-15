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
dic2[(1,1)] = 1
while que :
    level, y, x = que.popleft()
    for n_y, n_x in dic.get((y, x), []) :
        if visited[n_y][n_x] : continue
        visited[n_y][n_x] = level+1
        que.append((level+1, n_y, n_x))

# for a in visited :
#     print(*a)


