from collections import deque
import sys
input = sys.stdin.readline
M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]
direct_y = [0,1,0,-1]
direct_x = [1,0,-1,0]

def BFS() :
    Max = 0
    que = deque()
    for i in range(N) :
        for j in range(M) :
            if tomato[i][j] == 1 :
                que.append([i,j])

    while que :
        y, x = que.popleft()
        for i in range(4) :
            dy = direct_y[i] + y
            dx = direct_x[i] + x
            if dy < 0 or dy == N or dx < 0 or dx == M :
                continue
            if tomato[dy][dx] != 0 :
                continue
            tomato[dy][dx] = tomato[y][x] + 1
            que.append([dy, dx])
    for a in tomato :
        print(*a)
    for i in range(N) :
        for j in range(M) :
            if tomato[i][j] == 0 :
                print(-1)
                return
            if tomato[i][j] > Max :
                Max = tomato[i][j]
    print(Max-1)        


BFS()
