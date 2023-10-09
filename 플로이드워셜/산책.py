import sys
input = sys.stdin.readline
V, E = map(int, input().split())
INF = 21e8
adj = [[INF] * (V+1) for _ in range(V+1)]
for _ in range(E) :
    s, e, d = map(int, input().split())
    adj[s][e] = d
for k in range(1, V+1) :
    for i in range(1, V+1) :
        if i == k : continue
        for j in range(1, V+1) :
            if j == k : continue
            if adj[i][j] > adj[i][k] + adj[k][j] :
                adj[i][j] = adj[i][k] + adj[k][j]
Min = INF
for i in range(1, V+1) :
    if Min > adj[i][i] :
        Min = adj[i][i]
if Min == INF :
    print(-1)
else :
    print(Min)