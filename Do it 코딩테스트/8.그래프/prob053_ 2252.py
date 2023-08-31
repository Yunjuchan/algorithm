# import sys
# input = sys.stdin.readline
# N, M = map(int, input().split())
# adj = [[] for _ in range(N+1)]
# visited = [False] * (N+1)
# lst = [0] * (N+1)
# for _ in range(M) :
#     s, e = map(int, input().split())
#     adj[s].append(e)
#     lst[e] += 1

# while True :  
#     for i in range(1, N+1) :
#         if not visited[i] and lst[i] == 0 :
#             visited[i] = True
#             print(i, end=' ')
#             for x in adj[i] :
#                 lst[x] -= 1
#     if sum(visited) == N :
#         break

from collections import deque 

N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]
visited = [False] * (N+1)
lst = [0] * (N+1)
for _ in range(M) :
    s, e = map(int, input().split())
    adj[s].append(e)
    lst[e] += 1
que = deque()
for i in range(1, N+1) :
    if lst[i] == 0 :
        que.append(i)
while que : 
    x = que.popleft()
    print(x, end=' ')
    for i in adj[x] :
        lst[i] -= 1
        if lst[i] == 0 :
            que.append(i)