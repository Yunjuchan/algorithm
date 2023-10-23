from collections import deque
import sys
input = sys.stdin.readline
N = int(input().rstrip())
island = [list(map(int, input().split())) for _ in range(N)]
# island2 = [[21e8]*N for _ in range(N)]
island2 = [[9]*N for _ in range(N)]

def check(idx, y, x) :
    que = deque()
    que.append((y, x))
    while que :
        flag = 1
        y, x = que.popleft()
        island2[y][x] = 0
        for i in range(4) :
            dy = direct_y[i] + y
            dx = direct_x[i] + x
            if dy < 0 or dx < 0 or dy >= N or dx >= N : continue
            if island[dy][dx] == 1 :
                que.append((dy, dx))
                island[dy][dx] = -idx
            elif island[dy][dx] == 0 :
                flag = 0
        if flag == 0 :
            que2.append((-idx, y, x))
                

direct_y = [1,0,-1,0]
direct_x = [0,1,0,-1]
que2 = deque()
cnt = 1
for i in range(N) :
    for j in range(N) :
        if island[i][j] != 1 : continue
        island[i][j] = -cnt
        check(cnt, i, j)
        cnt += 1

ret = 21e8
while que2 :
    tp, y, x = que2.popleft()
    for i in range(4) :
        dy = direct_y[i] + y
        dx = direct_x[i] + x
        if dy < 0 or dx < 0 or dy >= N or dx >= N : continue

        if island2[dy][dx] == 9 :
            island[dy][dx] = tp
            island2[dy][dx] = island2[y][x] + 1
            que2.append((tp, dy, dx)) 
        else :
            if island[dy][dx] == tp : continue
            if ret > island2[dy][dx] + island2[y][x] :
                ret = island2[dy][dx] + island2[y][x]

print(ret)