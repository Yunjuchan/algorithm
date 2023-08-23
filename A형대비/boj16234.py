from collections import deque
def make_united(y, x) :
    direct_y = [0,0,1,-1]
    direct_x = [1,-1,0,0]
    visited[y][x] = True
    ret = [[y, x]]
    que = deque([[y,x]])
    while que :
        y, x = que.popleft()
        for i in range(4) : 
            dy = direct_y[i] + y
            dx = direct_x[i] + x
            if 0 <= dy < N and 0 <= dx < N :
                if not visited[dy][dx] and L <= abs(arr[y][x] - arr[dy][dx]) <= R :
                    visited[dy][dx] = True
                    que.append([dy,dx]) 
                    ret.append([dy,dx])
    return ret
N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
while True :
    
    visited = [[False]*N for _ in range(N)]
    united_list = []
    for i in range(N) :
        for j in range(N) :
            if not visited[i][j] :
                ret = make_united(i, j)
                if len(ret) > 1 :
                    united_list.append(ret)
                    
    if not united_list :
        break
    for u in united_list :
        level = 0
        for y, x in u :
            level += arr[y][x]
        level //= len(u)
        for y, x in u :
            arr[y][x] = level
    cnt += 1
print(cnt)