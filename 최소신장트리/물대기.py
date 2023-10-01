from heapq import heappop, heappush
import sys
input = sys.stdin.readline
N = int(input().rstrip())
INF = 21e8
water = [0]*N
que = []
visited = [False]*N
for i in range(N) :
    x = int(input().rstrip())
    water[i] = x
    heappush(que, [x, i])
arr = [list(map(int, input().split())) for _ in range(N)]
while que :
    w, now = heappop(que)
    if visited[now] : continue
    visited[now] = True
    for i in range(N) :
        if i == now : continue
        if not visited[i] and water[i] > arr[now][i] :
            water[i] = arr[now][i]
            heappush(que, [arr[now][i], i])
print(sum(water))