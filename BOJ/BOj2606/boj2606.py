from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
adj = [deque() for _ in range(N+1)]
for _ in range(M) : 
    s, e = map(int, input().split())
    adj[s].append(e)
    # adj[e].append(s)
def BFS(x) :
    cnt = 0
    que = deque()   
    que.append(x)
    while que :    
        a = que.popleft()
        if not visited[a] :
            visited[a] = True
            cnt += 1
            que += adj[a]
    return cnt
visited = [False] * (N+1)
print(BFS(1))