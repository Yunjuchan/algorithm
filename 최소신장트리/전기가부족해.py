from heapq import heappush, heappop
import sys
input = sys.stdin.readline
N, M, K = map(int, input().split())
lst = list(map(int, input().split()))
visited = [False] * (N+1)
adj = [[] for _ in range(N+1)]
que = []
result = 0
for _ in range(M) :
    u, v, w = map(int, input().split())
    adj[u].append([w, v])
    adj[v].append([w, u])
for i in lst :
    visited[i] = True
    for x in adj[i] :
        if not visited[x[1]] :
            heappush(que, x)
while sum(visited) < N :
    w, now = heappop(que)
    if visited[now] : continue
    result += w
    visited[now] = True
    for x in adj[now] :
        if not visited[x[1]] :
            heappush(que, x)
print(result)
