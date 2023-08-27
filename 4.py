from collections import deque
import copy
def melt(y, x) :
    global arr
    direct_y = [0,0,1,-1]
    direct_x = [1,-1,0,0]
    arr2 = copy.deepcopy(arr)

    que = deque()
    que.append([y, x])
    visited[y][x] = True
    
    while que :
        y, x = que.popleft()
        for i in range(4) :
            dy = direct_y[i] + y
            dx = direct_x[i] + x
            if arr[dy][dx] == 0 :
                arr2[y][x] -= 1
            elif not visited[dy][dx] :
                visited[dy][dx] = True
                que.append([dy, dx])
        if arr2[y][x] < 0 :
            arr2[y][x] = 0
            
    arr = copy.deepcopy(arr2)

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = 0

while True :
    flag = 0
    visited = [[False]*M for _ in range(N)]
    for i in range(1,N-1) :
        for j in range(1, M-1) :
            if arr[i][j] != 0 and not visited[i][j]:
                flag += 1
                if flag == 2 :
                    break

                melt(i, j)

        if flag == 2 :
            break

    if flag != 1 :
        break
    cnt += 1
    for a in arr :
        print(*a)

if flag == 2 :
    print(cnt)
else :
    print(0)
