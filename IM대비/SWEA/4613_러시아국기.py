def color(n1, n2) :
    cnt = 0
    for i in range(n1) :
        for j in range(M) :
            if arr[i][j] != 'W' :
                cnt += 1
    for i in range(n1, n2) :
        for j in range(M) :
            if arr[i][j] != 'B' :
                cnt += 1
    for i in range(n2, N) : 
        for j in range(M) :
            if arr[i][j] != 'R' :
                cnt += 1
    return cnt

T = int(input())
for tc in range(1, T+1) :
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    Min = 21e8
    for i in range(1, N-1) :
        for j in range(i+1, N) :
            ret = color(i, j)
            if ret < Min :
                Min = ret
    print(f'#{tc} {Min}')
