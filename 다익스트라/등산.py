from heapq import heappop, heappush
import sys
input = sys.stdin.readline
N, M, D, E = map(int, input().split())
H = [0] + list(map(int, input().split()))
adj = [[] for _ in range(N+1)]
INF = 21e13

for _ in range(M) :
    s, e, d = map(int, input().split())
    if H[s] > H[e] :
        # 시작점이 더 높으면
        adj[e].append([s, d])
    elif H[s] < H[e] :
        adj[s].append([e, d])

def dijk(start) :
    que = []
    dist = [INF] * (N+1)
    visited = [False] * (N+1)
    dist[start] = 0
    heappush(que, [0, start])
    while que :
        d, now = heappop(que)
        if visited[now] : continue
        visited[now] = True
        for next, next_d in adj[now] :
            if visited[next] : continue
            if dist[next] >= d + next_d :
                dist[next] = d + next_d 
                heappush(que, [dist[next], next])
    return dist[:]

up_dist = dijk(1)
down_dist = dijk(N)
Max = -INF
for i in range(1, N) :
    if up_dist[i] == INF or down_dist[i] == INF : continue
    tmp = H[i]*E - (up_dist[i]+down_dist[i]) * D
    if tmp > Max :
        Max = tmp
if Max == -INF :
    print('Impossible')
else :
    print(Max)
