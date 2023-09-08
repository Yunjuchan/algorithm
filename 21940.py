N, M = map(int, input().split())
INF = 21e8
adj = [[INF]*(N+1) for _ in range(N+1)]
for _ in range(M) :
    s, e, w = map(int, input().split())
    adj[s][e] = w
for i in range(1, N+1) :
    adj[i][i] = 0

for k in range(1, N+1) :
    for i in range(1, N+1) :
        if i == k : continue
        for j in range(1, N+1) :
            if j == k or j == i : continue
            adj[i][j] = min(adj[i][j], adj[i][k]+adj[k][j])
K = int(input())
lst = list(map(int, input().split()))
Min = INF
m_lst = []

for i in range(1, N+1) :
    tmp = 0
    for k in range(K) :
        if tmp < adj[lst[k]][i] + adj[i][lst[k]] < INF :
            tmp = adj[lst[k]][i] + adj[i][lst[k]]

    if Min > tmp :
        Min = tmp
        m_lst = [i]
    elif Min == tmp :
        m_lst.append(i)
print(*m_lst)

