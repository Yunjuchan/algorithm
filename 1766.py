from heapq import heappop, heappush
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
lst = [0]*(N+1)
adj = [[] for _ in range(N+1)]
que = []
for _ in range(M) :
    pre, post = map(int, input().split())
    adj[pre].append(post)
    lst[post] += 1
for i in range(1,N+1) :
    if lst[i] == 0 : 
        heappush(que, i)
while que :
    now = heappop(que)
    print(now, end=' ')
    for next in adj[now] :
        lst[next] -= 1
        if lst[next] == 0 :
            heappush(que, next)
            