from heapq import *
import sys
input = sys.stdin.readline
p, w = map(int, input().split())
c, v = map(int, input().split())
adj = [[] for _ in range(p)]

for _ in range(w) :
    a, b, d = map(int, input().split())
    adj[a].append((b, d))
    adj[b].append((a, d))

def dijk(x) :
    que = []
    heappush(que, (21e8, x))
    width = [0] * p
    while que :
        w, now = heappop(que)
        for next, next_w in adj[now] :
            if width[next] < min(next_w, w) :
                width[next] = min(next_w, w)
                heappush(que, (width[next], next))
    return width[:]

width_c = dijk(c)
result = width_c[v]
print(result)

