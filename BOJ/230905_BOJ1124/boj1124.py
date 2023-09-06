n, m ,r = map(int, input().split())
lst = list(map(int, input().split()))
INF = 21e8
adj = [[INF]*(n+1) for _ in range(n+1)]
for _ in range(r) :
    s, e, w = map(int, input().split())
    adj[s][e] = w
    adj[e][s] = w
for i in range(1,n+1) :
    for j in range(1,n+1) :
        for k in range(1,n+1) :
            adj[j][k] = min(adj[j][k], adj[j][i] +adj[i][k])
Max = 0
for i in range(1,n+1) :
    adj[i][i] = 0
    tmp = 0
    for j in range(1,n+1) :
        if adj[i][j] <= m :
            tmp += lst[j-1]
    if tmp > Max :
        Max = tmp
print(Max)