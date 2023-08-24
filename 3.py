C, R = map(int, input().split())
target = int(input())
direct_y = [1,0,-1,0]
direct_x = [0,1,0,-1]
d = 0
i = 1
y = x = 0
arr = [[0]*C for _ in range(R)]
arr[0][0] = 1

while i < R*C :
    dy = direct_y[d%4] + y
    dx = direct_x[d%4] + x
    if 0 <= dy < R and 0 <= dx < C and arr[dy][dx] == 0:
        arr[dy][dx] = i+1
        y = dy
        x = dx
        i += 1
    else :
        d += 1

for i in range(R) :
    for j in range(C) :
        if arr[i][j] == target :
            x, y = j+1, i+1
if target > R*C :
    print(0)
else :
    print(x, y)