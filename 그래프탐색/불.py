from collections import deque
T = int(input().rstrip())
direct_y = [1,0,-1,0]
direct_x = [0,1,0,-1]
def bfs(que) :
    while que :
        cnt, y, x = que.popleft()
        for i in range(4) :
            dy = direct_y[i] + y
            dx = direct_x[i] + x
            if dy < 0 or dx < 0 or dy >= N or dx >= M :
                if arr[y][x] == '@' : return cnt
                else : continue
            if arr[dy][dx] == arr[y][x] or arr[dy][dx] == '#': continue
            if arr[y][x] == '@' and arr[dy][dx] == '*' : continue
            arr[dy][dx] = arr[y][x]
            que.append((cnt+1, dy, dx))

    return 'IMPOSSIBLE'

for _ in range(T) :
    M, N = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    que = deque()
    for i in range(N) :
        for j in range(M) :
            if arr[i][j] == '*' :
                que.append((1, i, j))
            elif arr[i][j] == '@' :
                que.appendleft((1, i, j))
    print(bfs(que))

