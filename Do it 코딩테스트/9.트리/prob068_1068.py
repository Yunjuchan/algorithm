N = int(input())
par = list(map(int, input().split()))
d = int(input())
adj = [[] for _ in range(N)]
A = [0] * N
for i in range(N) :
    if par[i] == -1 : 
        root = i
        continue
    adj[i].append(par[i])
    adj[par[i]].append(i)
    A[par[i]] += 1
cnt = 0
def dfs(now) :
    if now == d :
        return
    global cnt
    visited[now] = True
    for i in adj[now] :
        if visited[i] or i == d : continue
        if adj[i] == [now] :
            cnt += 1
        dfs(i)
visited = [False] * N
dfs(root)
if A[par[d]] == 1 :
    cnt += 1
print(cnt)