from collections import deque
import copy
def bfs(y, x) :
    visited = [[False]*N for _ in range(N)]
    direct_x = [0,0,1,-1]
    direct_y = [1,-1,0,0]
    que = deque()
    que.append([y, x, 0])
    while que :
        y, x, level = que.popleft()
        for i in range(4) :
            dy = direct_y[i] + y
            dx = direct_x[i] + x
            if 0 <= dy < N and 0 <= dx < N :
                if not visited[dy][dx] :
                    if arr[dy][dx] == 3 :
                        return level + 1
                    visited[dy][dx] = True
                    que.append([dy, dx, level + 1])

def abc(level, start) :
    global Min
    if level == M :
        ret = 0
        new_dist = []
        for i in range(M) :
            new_dist.append(dist[path_list[i]])
        for x in zip(*new_dist) :
            ret += min(x)
        if ret < Min :
            Min = ret
        return

    for i in range(start, len(chicken)) :
        path_list.append(i)
        abc(level+1, i+1)
        path_list.pop()

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
house = []
chicken = []
for i in range(N) :
    for j in range(N) :
        if arr[i][j] == 1 :
            house.append([i, j])
        elif arr[i][j] == 2 :
            chicken.append([i, j])
dist = [[0]*len(house) for _ in range(len(chicken))]
for i in range(len(chicken)) :
    for j in range(len(house)) :
        dist[i][j] += abs(chicken[i][0] - house[j][0]) + abs(chicken[i][1] - house[j][1])
path_list = []
Min = 21e8
abc(0,0)
print(Min)


