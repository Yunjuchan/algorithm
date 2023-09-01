from collections import deque
from heapq import heappush, heappop
def dijk(a) :
    visited = [False] * (N+1)
    INF = 21e8
    x = [INF]*(N+1)
    x[X] = 0
    que = []
    heappush(que, [x[X], X])
    while que : 
        now_v, now = heappop(que)
        if visited[now] :
            continue
        visited[now] = True
        for next, v in a[now] :
            if x[next] > v+now_v :
                x[next] = v+now_v
                heappush(que, [x[next], next])
    return x

N, M, X = map(int, input().split())

adj1 = [[] for _ in range(N+1)]
adj2 = [[] for _ in range(N+1)]

for _ in range(M) :
    s, e, w = map(int, input().split())
    adj1[s].append([e, w])
    adj2[e].append([s, w])

result = [0]*(N+1)
a = dijk(adj1)
b = dijk(adj2)
for i in range(1,N+1) :
    result[i] += a[i]+b[i]
print(max(result))
