from heapq import heappop, heappush
from collections import deque
import sys
input = sys.stdin.readline
N = int(input().rstrip())
island = [list(map(int, input().split())) for _ in range(N)]
island2 = [[21e8]*N for _ in range(N)]

def check(idx, y, x) :
    que = deque()
    que.append((y, x))
    while que :
        y, x = que.popleft()
        island2[y][x] = 0
        island[y][x] = -idx
        for i in range(4) :
            dy = direct_y[i] + y
            dx = direct_x[i] + x
            if dy < 0 or dx < 0 or dy >= N or dx >= N : continue
            if island[dy][dx] == 0 :
                heappush(pq, (0, -idx, y, x))
            elif island[dy][dx] == 1 :
                island[dy][dx] = 0
                que.append((dy, dx))


direct_y = [1,0,-1,0]
direct_x = [0,1,0,-1]
pq = []
cnt = 1
for i in range(N) :
    for j in range(N) :
        if island[i][j] != 1 : continue
        island[i][j] = 0
        check(cnt, i, j)
        cnt += 1

for a in island :
    print(*a)

while pq :
    ret = 21e8
    cnt, tp, y, x = heappop(pq)
    print(tp)
    for i in range(4) :
        dy = direct_y[i] + y
        dx = direct_x[i] + x
        if dy < 0 or dx < 0 or dy >= N or dx >= N : continue
        if island2[dy][dx] == 21e8  :
            island2[dy][dx] = cnt + 1
            heappush(pq, (cnt+1, dy, dx))
        else :
            if ret > island2[dy][dx] + cnt :
                ret = island2[dy][dx] + cnt
    if ret != 21e8 :
        break
print()
for a in island2 :
    print(*a)
print(ret)
            