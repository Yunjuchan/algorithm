from copy import deepcopy
direct_y = [0,0,1,-1]
direct_x = [1,-1,0,0]
T = int(input())
def popping(y, x) :
    cnt = balloons[y][x]
    for i in range(4) :
        dy = direct_y[i] + y
        dx = direct_x[i] + x
        if 0 <= dy < N and 0 <= dx < M :
            cnt += balloons[dy][dx]
    return cnt

for tc in range(1, T+1) :
    Max = 0
    N, M = map(int, input().split())
    balloons = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N) :
        for j in range(M) :
            if balloons[i][j] != 0 :
                if popping(i,j) > Max :
                    Max = popping(i,j)
    print(Max)