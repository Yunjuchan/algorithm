from collections import deque
def bfs(x) :
    visited = [[False]*(N+1) for _ in range(N+1)]
    que = deque([[x, 1]])
    while que :
        now, level = que.popleft()
        for i in range(1, N+1) :
            if not visited[x][i] and adj[x][i] :
                if adj[now][i] == 0 :
                    visited[now][i] = True
                    visited[i][now] = True
                    que.append([i, level+adj[x][i]])
                    adj[now][i] = level+adj[x][i]
                    adj[i][now] = level+adj[x][i]

N, M = map(int, input().split())

adj = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M) :
    s, e = map(int, input().split())
    adj[s][e] = 1
    adj[e][s] = 1
for i in range(1, N+1) :
        bfs(i)
for a in adj :
    print(*a)
