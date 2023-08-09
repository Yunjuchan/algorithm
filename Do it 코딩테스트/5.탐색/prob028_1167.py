import sys
input = sys.stdin.readline
from collections import deque
N = int(input())
edge_list = [[] for _ in range(N+1)]
for _ in range(N) :
    X = deque(map(int, input().split()))
    start = X.popleft()
    while True :
        end = X.popleft()
        
        if end == -1 :
            break
        else :
            dist = X.popleft() 
            edge_list[start].append([end, dist])

distance = [0] * (N+1)
def BFS(start) :
    que = deque([])
    que.append(start)
    visited[start] = True
    while que :
        now = que.popleft()
        for edge in edge_list[now] :
            if not visited[edge[0]] :
                que.append(edge[0])
                visited[edge[0]] = True
                distance[edge[0]] = distance[now] + edge[1]

## 시간초과났음
# for i in range(1, N+1) :
#     visited = [False] * (N+1)
#     distance = [0] * (N+1)
#     BFS(i)
#     if max(distance) > radius :
#         radius = max(distance) 
# print(radius)

visited = [False] * (N+1)
distance = [0] * (N+1)
BFS(1)
Max = 1
for i in range(1, N+1) :
    if distance[Max] < distance[i] :
        Max = i
visited = [False] * (N+1)
distance = [0] * (N+1)
BFS(Max)
print(max(distance))

