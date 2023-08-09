## 카운트를 세는 것이 아니라
## 미로의 길을 1씩 더해가면서 모든 길을 방문하는 방법으로 풀이

from collections import deque 
N, M = map(int, input().split())
def BFS(y, x) :
    que = deque([])
    visited_xy[y][x] = True
    que.append([y, x])
    while que :

        y, x = que.popleft()
        for i in range(4) :
            dy = direct_y[i] + y
            dx = direct_x[i] + x
            if 0 <= dy < N and 0 <= dx < M :
                if miro[dy][dx] == 1 and visited_xy[dy][dx] == False:
                    visited_xy[dy][dx] = True
                    miro[dy][dx] = miro[y][x] + 1
                    que.append([dy, dx])

direct_y = [0,0,1,-1]
direct_x = [1,-1,0,0]
miro = [list(map(int, list(input()))) for _ in range(N)]
visited_xy = [[False]*M for _ in range(N)] 
BFS(0,0)
print(miro[N-1][M-1])
