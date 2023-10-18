N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
res = 0
for i in range(N) :
    for j in range(N) :
        res += arr[i][j]
result = 0
flag = 0
visited = [[0]*N for _ in range(N)]
for k in range(N) :
    for i in range(N) :
        if arr[i][k] == 0 : continue
        for j in range(N) :
            if k == i or k == j : continue
            if arr[k][j] == 0 : continue
            if arr[i][j] == arr[k][i] + arr[j][k] :
                arr[i][j] = 0
            elif arr[i][j] > arr[k][i] + arr[j][k] :
                flag = 1

for i in range(N) :
    for j in range(N) :
        result += arr[i][j]
if flag == 1 :
    print(-1)
else :
    print(result//2)
