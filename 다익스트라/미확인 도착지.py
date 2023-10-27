import sys
from heapq import heappush, heappop
input = sys.stdin.readline
T = int(input().rstrip())
def dijk(s, g, h) :
    que = []
    heappush(que, (0, s))
    dist[s][1] = 0
    while que :
        d, now = heappop(que)
        if dist[now][1] < d : continue
        for next, next_d in adj[now] :
            if dist[next][1] > d + next_d :
                dist[next] = [dist[now][0], d + next_d]
                
                if (now == g and next == h) or (now == h and next == g) :
                    dist[next][0] = 1
                heappush(que, (dist[next][1], next))
                
            elif dist[next][1] == d + next_d :
                if dist[now][0] or (now == g and next == h) or (now == h and next == g):
                    dist[next][0] = 1

for _ in range(T) :
    n, m, t = map(int, input().split())
    adj = [[] for _ in range(n+1)]
    s, g, h = map(int, input().split())
    dist = [[0, 21e8] for _ in range(n+1)]
    result = []
    for _ in range(m) :
        a, b, d = map(int, input().split())
        adj[a].append([b, d])
        adj[b].append([a, d])
    dijk(s, g, h)
    
    for _ in range(t) :
        x = int(input().rstrip())
        if dist[x][0] == 1 :
            result.append(x)
    result.sort()
    print(*result)

