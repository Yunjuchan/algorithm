direct_y = [0,0,1,-1,1,-1,1,-1]
direct_x = [1,-1,0,0,1,1,-1,-1]

N = int(input())
arr = [list(input()) for _ in range(N)]
arr2 = [[0]*N for _ in range(N)]
for y in range(N) :
    for x in range(N) :
        if arr[y][x].isdigit() :
            for i in range(8) :
                arr2[y][x] = -1 
                dy = direct_y[i] + y
                dx = direct_x[i] + x
                if 0 <= dy < N and 0 <= dx < N :
                    if arr2[dy][dx] >= 0 :
                        arr2[dy][dx] += int(arr[y][x])
for i in range(N) : 
    for j in range(N) :
        if arr2[i][j] == -1 :
            arr2[i][j] = '*'
        elif arr2[i][j] >= 10 :
            arr2[i][j] = 'M'
        else :
            arr2[i][j] = str(arr2[i][j])
for a in arr2 :
    print(*a, sep='')