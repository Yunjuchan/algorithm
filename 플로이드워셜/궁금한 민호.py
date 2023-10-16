N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
result = 0
visited = [[0]*N for _ in range(N)]
for k in range(N) :
    for i in range(N) :
        for j in range(N) :
            if arr[i][j] == arr[k][i] + arr[j][k] :
                visited[i][j] = 0
                visited[i][k] = arr[i][k]
                visited[k][j] = arr[k][j]
for i in range(N) :
    for j in range(N) :
        result += visited[i][j]
print(result//2)
for a in visited :
    print(*a)