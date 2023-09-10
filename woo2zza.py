from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [input() for _ in range(N)]

def bfs(y, x, level) :
    global cnt
    que = deque()
    que.append([y, x])
    while que :
        c_y, c_x = que.popleft()  
        visited[c_y][c_x] = level
        n_y, n_x = command(c_y, c_x, arr[c_y][c_x])
        if visited[n_y][n_x] != -1 :
            if visited[n_y][n_x] == level :
                cnt += 1
            return
        else :
            que.append([n_y, n_x])
        
def command(y, x, c) :
    if c == 'D' :
        y += 1
    elif c == 'U' :
        y -= 1
    elif c == 'R' :
        x += 1
    else :
        x -= 1
    return y, x

visited = [[-1]*M for _ in range(N)]

cnt = level = 0
for i in range(N) :
    for j in range(M) :
        if visited[i][j] == -1:
            bfs(i, j, level)
            level += 1
print(cnt)
