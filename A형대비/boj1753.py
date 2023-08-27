## 인접행렬 실패

# from collections import deque
# V, E = map(int, input().split())
# start = int(input())
# INF = 21e8
# adj = [[INF]*(V+1) for _ in range(V+1)]
# for i in range(E) :
#     s, e, w = map(int, input().split())
#     adj[s][e] = w
# def abc(start, w) :
#     visited = [False] * (V+1)
#     que = deque()
#     que.append([start, w])
#     while que :
#         x, w = que.popleft()
#         visited[x] = True
#         if adj[start][x] > w :
#             adj[start][x] = w
#         for i in range(1, V+1) :
#             if not visited[i] and adj[x][i] != INF :
#                 que.append([i, w + adj[x][i]])
            

# abc(start, 0)
# for i in range(1,V+1) :
#     if adj[start][i] == INF :
#         print('INF')
#     else :
#         print(adj[start][i])


# from collections import deque
# V, E = map(int, input().split())
# start = int(input())
# INF = 21e8
# adj = [[] for _ in range(V+1)]
# dist = [INF]*(V+1)
# dist[start] = 0
# for i in range(E) :
#     s, e, w = map(int, input().split())
#     adj[s].append([e,w])
#     if s == start :
#         dist[e] = w

# def abc(start, w) :
#     visited = [False] * (V+1)
#     que = deque()
#     que.append([start, w])
#     while que :
#         x, w = que.popleft()
#         visited[x] = True
#         for i in adj[x] :
#             if dist[i[0]] > w + i[1] :
#                 dist[i[0]] = w + i[1]
#             if not visited[i[0]] :
#                 que.append([i[0], i[1] + w])
            
# abc(start, 0)
# for i in range(1,V+1) :
#     if dist[i] == INF :
#         print('INF')
#     else :
#         print(dist[i])

import heapq
import sys
input = sys.stdin.readline
V, E = map(int, input().split())
start = int(input())                 
INF = 21e8
graph = [[] for _ in range(V+1)] 
distance = [INF] * (V+1)
for _ in range(E):
    s, e, w = map(int, input().split())
    graph[s].append([e, w])             

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) 
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q) 
        if distance[now] < dist: 
            continue               
        for i in graph[now]:     
            if dist+i[1] < distance[i[0]]: 
                distance[i[0]] = dist+i[1]   
                heapq.heappush(q, (dist+i[1], i[0]))
dijkstra(start)
for i in range(1, V+1) :
    if distance[i] == INF :
        print('INF')
    else :
        print(distance[i])