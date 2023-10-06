def dijk(start) :
    que = []
    dist = [INF] * (V+1)
    dist[start] = 0
    visited = [False] * (V+1)
    heappush(que, [0, start])
    while que :
        w, now = heappop(que)
        if visited[now] : continue
        visited[now] = True
        for next, next_w in adj[now] :
            if dist[next] > w + next_w :
                dist[next] = w + next_w
                heappush(que, [dist[next], next])
    return dist

def azumma_dijk(start, end) :
    que = []
    dist2 = [INF] * (V+1)
    dist2[start] = 0
    visited = [False] * (V+1)
    heappush(que, [0, start])
    while que :
        w, now = heappop(que)
        
        if visited[now] : continue
        visited[now] = True
        if now == end :
            return w
        for next, next_w in adj[now] :
            if dist2[next] > w + next_w :
                dist2[next] = w + next_w
                heappush(que, [dist2[next], next])
    return -1
    

from heapq import heappush, heappop
import sys
input = sys.stdin.readline
INF = 21e8
V, E = map(int, input().split())
adj = [[] for _ in range(V+1)]
for _ in range(E) :
    s, e, w = map(int, input().split())
    adj[s].append([e, w])
    adj[e].append([s, w])
azumma_route = list(map(int, input().split()))
result = []
azumma = 0
me = int(input().rstrip())
my_dist = dijk(me)
current_time = 0
if azumma_route[0] == me :
    result.append(me)
i = 0
j = 1
while j < 10 :
    x = azumma_dijk(azumma_route[i], azumma_route[j])
    if x == -1 :
        j += 1
        continue
    current_time += x
    if current_time >= my_dist[azumma_route[j]] :
        result.append(azumma_route[j])
    i, j = j, j+1 
    

result.sort()
if not result :
    print(-1)
else :
    print(result[0])