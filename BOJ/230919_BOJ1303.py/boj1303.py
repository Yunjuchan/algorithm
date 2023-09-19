from collections import deque
import sys
input = sys.stdin.readline
direct_y = [0,1,0,-1]
direct_x = [1,0,-1,0]
M, N = map(int, input().split())
arr = [input() for _ in range(N)]
visited = [[False]*M for _ in range(N)]
cnt = [0,0]
def bfs(y, x, tp) :
    que = deque()
    que.append([y, x])
    c = 1
    while que :
        y, x = que.popleft()
        for i in range(4) :
            dy = direct_y[i] + y
            dx = direct_x[i] + x
            if 0 <= dy < N and 0 <= dx < M :
                if not visited[dy][dx] :
                    if tp == 0 and arr[dy][dx] == 'W':
                        visited[dy][dx] = True
                        c += 1
                        que.append([dy, dx])
                    elif tp == 1 and arr[dy][dx] == 'B' :
                        visited[dy][dx] = True
                        c += 1
                        que.append([dy, dx])   
    cnt[tp] += c**2

for i in range(N) :
    for j in range(M) :
        if not visited[i][j] :
            if arr[i][j] == 'W' :
                visited[i][j] = True
                bfs(i, j ,0)
            else :
                visited[i][j] = True
                bfs(i, j ,1)
print(*cnt)
    

