from heapq import heappush, heappop
import sys
input = sys.stdin.readline
N, M, K = map(int, input().split())
adj = [[] for _ in range(N+1)]
INF = 21e13

for _ in range(M) :
    s, e, d = map(int, input().split())
    adj[e].append([s, d])

R = list(map(int, input().split()))

que = []
dist = [INF] * (N+1)
visited = [False] * (N+1)
for i in R :
    heappush(que,[0, i])
    dist[i] = 0

while que :
    d, now = heappop(que)
    if visited[now] : continue
    visited[now] = True
    for next, next_d in adj[now] :
        if dist[next] > d+next_d :
            dist[next] = d+next_d
            heappush(que, [dist[next], next])
Max = -1
for i in range(1, N+1) :
    if dist[i] > Max :
        Max = dist[i]
        Max_i = i
print(Max_i)
print(Max)
