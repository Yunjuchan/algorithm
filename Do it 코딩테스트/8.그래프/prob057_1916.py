from heapq import heappop, heappush
N = int(input())
M = int(input())
adj = [[] for _ in range(N+1)]
INF = 21e8
cost = [INF] * (N+1)
for _ in range(M) :
    a, b, w = map(int, input().split())
    adj[a].append([b, w])
start, end = map(int, input().split())
cost[start] = 0

def dijk(a) :
    visited = [False]*(N+1)
    q = [[cost[a],a]]
    while q :
        now_w, now = heappop(q)
        if visited[now] :
            continue
        visited[now] = True
        for next, w in adj[now] :
            if cost[next] > now_w + w :
                cost[next] = now_w + w
                heappush(q, [cost[next], next])

dijk(start)
print(cost[end])