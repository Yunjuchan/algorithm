from collections import deque
import sys
input = sys.stdin.readline
N, M, K, X = map(int, input().split())
adj = [[] for _ in range(N+1)]
for _ in range(M) :
    s, e = map(int, input().split())
    adj[s].append(e)

# visited = [False] * (N+1)
# INF = 21e8
# lst = [INF] * (N+1)
# def dfs(now, level) :
#     if lst[now] > level :
#         lst[now] = level
#     for i in adj[now] :
#         if not visited[i] :
#             visited[i] = True 
#             dfs(i, level+1)
#             visited[i] = False
# visited[X] = True
# dfs(X, 0)

# flag = 0
# for i in range(N+1) :
#     if lst[i] == K :
#         flag = 1
#         print(i)
# if flag == 0 :
#     print(-1)


def bfs(now) :
    visited= [False] * (N+1)
    que = deque()
    que.append([now, 0])
    visited[X] = True
    while que :
        x, level = que.popleft()
        if level == K :
            lst.append(x)
            continue

        for i in adj[x] :
            if not visited[i] :
                visited[i] = True 
                que.append([i,level+1])           
lst = []
bfs(X)
if not lst :
    print(-1)
else :
    lst.sort()
    for i in lst :
        print(i)

    