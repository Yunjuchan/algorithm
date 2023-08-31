## 가장 늦게 도착하는 친구의 카운팅이 필요

import sys
from collections import deque
input = sys.stdin.readline
# 사이클 x 일반통행

def bfs(x) :
    global visited
    que = deque()
    que.append([x, 0])
    while que :
        now, time = que.popleft()
        for i, t in adj[now] :
            lst[i] -= 1
            if T[i] < time+t :
                T[i] = time+t
            if lst[i] == 0 :
                que.append([i, T[i]])

N = int(input())
M = int(input())
adj = [[] for _ in range(N+1)]
A = [[] for _ in range(N+1)]
lst = [0] * (N+1)
T = [0] * (N+1)
for _ in range(M) :
    s, e, t = map(int, input().split())
    A[e].append([s,t])
    adj[s].append([e,t])
    lst[e] += 1 
    

x, y = map(int, input().split())

bfs(x)
print(T[y])
que = deque([[y, T[y]]])
visited = [[False] * (N+1) for _ in range(N+1)]
cnt = 0
while que :
    a, t = que.popleft()
    for i, t2 in A[a] :
        if T[i] == t - t2 and not visited[i][a]:
            cnt += 1
            visited[i][a] = True
            que.append([i, T[i]])
print(cnt)

