from heapq import heappush, heappop
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]
for _ in range(M) :
    s, e, w = map(int, input().split())
    adj[s].append([w, e])
    adj[e].append([w, s])
a, b = map(int, input().split())
H = list(map(int, input().split()))
X = [False] * (N+1)
D = [21e8] * (N+1)
visited = [False] * (N+1)
for i in list(map(int, input().split())) :
    X[i] = True
que = []
for i in H :
    D[i] = 0
    heappush(que, (0, i, i))
while que :
    w, root, now = heappop(que) 
    if X[now] : break
    if visited[now] : continue
    visited[now] = True
    for next_w, next in adj[now] :
        if D[next] > next_w+w :
            D[next] = next_w+w
            heappush(que, (D[next], root, now))
print(root)
