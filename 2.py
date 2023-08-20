from collections import deque 
N, M = map(int, input().split())
adj = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M) :
    s, e = map(int, input().split())
    adj[s][e] = 1
    adj[e][s] = 1
def bfs(x) :
    que = deque()
    que.append([x, 1])
    while que :
        print(que)
        now, level = que.popleft()
        for i in range(N) :
            if adj[now][i] == 1 :
                que.append(i, level+1)
                if  adj[i][x] == 0:
                    adj[x][i] = level
                    adj[i][x] = level
bfs(1)
print(adj)
