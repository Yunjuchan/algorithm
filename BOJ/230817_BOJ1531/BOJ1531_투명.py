N, M = map(int, input().split())
arr = [[0]*100 for _ in range(100)]
for i in range(N) :
    y1, x1, y2, x2 = map(int, input().split())
    for i in range(y1-1, y2) :
        for j in range(x1-1, x2) :
            arr[i][j] += 1
cnt = 0
for i in range(100) :
    for j in range(100) :
        if arr[i][j] > M :
            cnt += 1
print(cnt)