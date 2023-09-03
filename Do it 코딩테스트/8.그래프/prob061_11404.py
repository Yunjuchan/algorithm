N = int(input())
M = int(input())
INF = 21e8
adj = [[INF]*(N+1) for _ in range(N+1)]
for i in range(N+1) :
    adj[i][i] = 0
for _ in range(M) :
    s, e, w = map(int, input().split())
    if adj[s][e] > w :
        adj[s][e] = w
for i in range(1,N+1) :
    for j in range(1,N+1) :
        for k in range(1,N+1) :
            adj[j][k] = min(adj[j][k], adj[j][i] + adj[i][k])
for i in range(N+1) :
    for j in range(N+1) :
        if adj[i][j] == INF :
            adj[i][j] = 0
for a in adj[1:] :
    print(*a[1:])