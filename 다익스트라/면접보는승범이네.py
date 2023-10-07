from heapq import heappush, heappop
import sys
input = sys.stdin.readline
N, M, K = map(int, input().split())
adj = [[] for _ in range(N+1)]
INF = 21e8

for _ in range(M) :
    s, e, d = map(int, input().split())
    adj[e].append([s, d])

L = list(map(int, input().split())) 

def dijk(start) :
    que = []
    dist = [INF] * (N+1)
    dist[start] = 0
    visited = [False] * (N+1)
    heappush(que, [0, start])
    while que :
        d, now = heappop(que)
        if visited[now] : continue
        visited[now] = True
        for next, next_d in adj[now] :
            if dist[next] > d+next_d :
                dist[next] = d+next_d
                heappush(que, [dist[next], next])
    for i in range(1, N+1) :
        result_dist[i] = min(dist[i], result_dist[i])
    return 

result_dist = [INF] * (N+1)
for i in L :
    dijk(i)
Max = 0
for i in range(1, N+1) :
    if result_dist[i] > Max :
        Max = result_dist[i]
        Max_i = i
print(Max_i)
print(Max)