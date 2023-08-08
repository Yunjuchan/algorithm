def retangle(y1, x1, y2, x2) :
    for i in range(y1, y2) :
        for j in range(x1, x2) :
            arr[i][j] += 1

arr = [[0] * 101 for _ in range(101)]
cnt = 0
for i in range(4) :
    retangle(*map(int, input().split()))
for y in range(101) :
    for x in range(101) :
        if arr[y][x] > 0 :
            cnt += 1
print(cnt)
