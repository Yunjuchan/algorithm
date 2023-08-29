from collections import deque
import sys
input = sys.stdin.readline
def bfs(x) :
    visited = [False]*(N+1)
    que = deque()
    que.append(x)
    visited[x] = True
    while que :
        a = que.popleft()
        max_i[x] += 1
        for i in adj[a] :
            if not visited[i] :
                visited[i] = True 
                que.append(i)

N, M = map(int, input().split())

adj = [[] for _ in range(N+1)]
for _ in range(M) :
    a, b = map(int, input().split()) 
    adj[b].append(a)

max_i = [0]*(N+1)
for i in range(1,N+1) :
    bfs(i)
                
for i in range(N+1) :
    if max_i[i] == max(max_i) :
        print(i, end=' ')