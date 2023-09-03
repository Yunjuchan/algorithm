N, M = map(int, input().split())
INF = 21e8
adj = [[INF]*(N+1) for _ in range(N+1)]
for _ in range(M) :
    s, e = map(int, input().split())
    adj[s][e] = 1
    adj[e][s] = 1
for i in range(1, N+1) :
    adj[i][i] = 0 
for i in range(1,N+1) :  
    for j in range(1,N+1) :
        for k in range(1, N+1) :
            adj[j][k] = min(adj[j][k], adj[j][i]+adj[i][k])

Min = INF
p = -1
for i in range(1,N+1) :
    if Min > sum(adj[i][1:]) :
        Min = sum(adj[i][1:])
        p = i
print(p)