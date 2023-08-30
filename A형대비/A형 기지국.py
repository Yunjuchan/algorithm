## 위에 있을 때 i-N-1 , i-N, i-N+1, i-1, i+N, i+1
## 아래 있을 때 i-1, i-N, i+1, i+N-1, i+N, i+N+1

def dfs(level, Sum, lst) :
    global Max, Max_path
    if level == 3 :
        if Sum > Max :
            Max = Sum
            Max_path = path[:]
        return
    for i in lst :
        if 0 <= i < N*M and not visited[i] :
            visited[i] = True
            path.append(i)
            dfs(level+1, Sum+arr[i], lst+a2[i])
            path.pop()
            visited[i] = False
T = int(input())
for tc in range(1, T+1) :
    M, N = map(int, input().split())
    arr = []
    for _ in range(M) :
        arr += list(map(int, input().split()))

    a2 = [[] for _ in range(N*M)]
    for i in range(N*M) :
        if i % N == 0 :
            a2[i] = [i-N, i-N+1, i+N, i+1]
        elif i % N == N-1 :
            if N % 2 == 1 :
                a2[i] = [i-N-1 , i-N, i-1, i+N]
            else :
                a2[i] = [i-1, i-N, i+N-1, i+N]
        elif i % N % 2 == 0 :   # 위에 있을 때
            a2[i] = [i-N-1 , i-N, i-N+1, i-1, i+N, i+1]
        elif i % N % 2 == 1 :
            a2[i] = [i-1, i-N, i+1, i+N-1, i+N, i+N+1]

    visited = [False] * N * M
    Max = 0
    for i in range(N*M) :
        visited[i] = True
        path = [i]
        dfs(0, arr[i], a2[i])
        visited[i] = False
    print(f'#{tc} {Max}')
    print(Max_path)
