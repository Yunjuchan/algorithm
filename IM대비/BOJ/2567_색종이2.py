## 다이렉트 기법
def draw(x, y) :
    for i in range(10) :
        for j in range(10) :
            arr[y+i][x+j] = 1
def is_edge(x, y, i) :
    dy = direct_y[i] + y
    dx = direct_x[i] + x
    if arr[dy][dx] == 0 :
        return 1
    return 0
    
arr = [[0]*101 for _ in range(101)]
N = int(input())
direct_y = [0,0,1,-1]
direct_x = [1,-1,0,0]
cnt = 0
for i in range(N) :
    x, y = map(int, input().split())
    draw(x, y)

for y in range(101) :
    for x in range(101) :
        if arr[y][x] == 1 :
            for i in range(4) :
                cnt += is_edge(x, y, i)
print(cnt)