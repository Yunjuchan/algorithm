from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = 21e8
T = int(input().rstrip())

for _ in range(T) :
    
    n, d, c = map(int, input().split())
    dist = [INF] * (n+1)
    adj = [[] for _ in range(n+1)]
    que = []
    
    for _ in range(d) :
        a, b, s = map(int, input().split())
        adj[b].append((a, s))
    
    heappush(que, (0, c))
    dist[c] = 0

    while que :
        t, now = heappop(que)
        if dist[now] < t : continue
        for next, next_t in adj[now] :
            if dist[next] > t + next_t :
                dist[next] = t + next_t
                heappush(que, (dist[next], next))
    cnt, max = 0, 0
    for x in dist :
        if x == INF : continue
        cnt += 1
        if max < x :
            max = x
    print(cnt, max)