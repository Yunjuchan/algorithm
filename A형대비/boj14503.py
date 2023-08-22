N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
direct_y = [-1,0,1,0]
direct_x = [0,1,0,-1]
def clean(y, x, d) :
    cnt = 0
    while True :
        flag = 0
        if arr[y][x] == 0 :
            cnt += 1
            arr[y][x] = -1
        for i in range(4) :
            dy = direct_y[i] + y
            dx = direct_x[i] + x
            if 0 <= dy < N and 0 <= dx < M :
                if arr[dy][dx] == 0 :
                    flag = 1
                    break
        if flag == 0 :
            y -= direct_y[d%4]
            x -= direct_x[d%4]
            if arr[y][x] == 1 :
                return cnt
        else :
            d -= 1
            move_y = direct_y[d%4] + y
            move_x = direct_x[d%4] + x
            if arr[move_y][move_x] == 0 :
                y = move_y
                x = move_x
ret = clean(r, c, d)
print(ret)