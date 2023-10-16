from heapq import heappush, heappop
import sys
input = sys.stdin.readline
N = int(input().rstrip())
M = int(input().rstrip())
INF = 21e8
que = []
dist = [INF] * (N+1)
adj = [[] for _ in range(N+1)]
adj2 = [[] for _ in range(N+1)]
for _ in range(M) :
    s, e, w = map(int, input().split())
    adj[s].append((w, e))
    adj2[e].append((w, s))
start, end = map(int, input().split())
dist[start] = 0
heappush(que, [0, start])
while que :
    w, now = heappop(que)
    if now == end :
        break
    for next_w, next in adj[now] :
        if dist[next] > w + next_w :
            dist[next] = w + next_w
            heappush(que, (dist[next], next))
print(w)
que = []
heappush(que, ([end], end))
while que :
    path, now = heappop(que)
    if now == start :
        break
    for next_w, next in adj2[now] :
        if dist[now] == dist[next] + next_w :
            heappush(que, ([next]+path[:], next))
print(len(path))
print(*path)