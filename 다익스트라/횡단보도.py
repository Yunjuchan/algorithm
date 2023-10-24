from heapq import heappush, heappop
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
time = [21e13] * (N+1)
que = []
adj = [[] for _ in range(N+1)]
for i in range(M) :
    a, b = map(int, input().split())
    adj[a].append((b, i))
    adj[b].append((a, i))
heappush(que, (0, 1))
time[1] = 0
while que :
    now_t, now = heappop(que)
    if now_t > time[now] : continue
    if now == N :
        break
    for next, r in adj[now] :
        if now_t % M > r : 
            tmp = (time[now] // M + 1) * M + r + 1
        else :
            tmp = (time[now] // M) * M + r + 1
            
        if time[next] > tmp :
            time[next] = tmp
            heappush(que, (time[next], next))
print(now_t)