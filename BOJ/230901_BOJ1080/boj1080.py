def change() :
    cnt = 0
    for i in range(N-2) :
        for j in range(M-2) :
            if arr[i][j] != arr2[i][j] :
                cnt += 1
                for y in range(3) :
                    for x in range(3) :
                        if i+y >= N or j+x >= M :
                            cnt = -1
                            return cnt
                        arr[i+y][j+x] += 1
                        arr[i+y][j+x] %= 2
    return cnt

N, M = map(int, input().split()) 
arr = [list(map(int, input())) for _ in range(N)]
arr2 = [list(map(int, input())) for _ in range(N)]
cnt = change()
for i in range(N) :
    for j in range(M) :
        if arr[i][j] != arr2[i][j] :
            cnt = -1
            break
    if cnt == -1 :
        break
print(cnt)
