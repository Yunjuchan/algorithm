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