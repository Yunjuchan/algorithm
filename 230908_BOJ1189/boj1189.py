import sys
input = sys.stdin.readline
R, C, K = map(int, input().split())
direct_y = [0,0,-1,1]
direct_x = [1,-1,0,0]
arr = [list(input()) for _ in range(R)]
start_y, start_x = R-1, 0
visited = [[False] * C for _ in range(R)]
def dfs(y, x, level) :
    global cnt
    if y ==  0 and x == C-1 and level != K :
        return
    
    if level == K :
        if y ==  0 and x == C-1 :
            cnt += 1
        return
    visited[y][x] = True 
    for i in range(4) :
        dy = direct_y[i] + y
        dx = direct_x[i] + x
        if 0 <= dy < R and 0 <= dx < C :
            if not visited[dy][dx] and arr[dy][dx] == '.' :
                visited[dy][dx] = True
                dfs(dy, dx, level+1)
                visited[dy][dx] = False
cnt = 0
dfs(start_y, start_x, 1)
print(cnt)