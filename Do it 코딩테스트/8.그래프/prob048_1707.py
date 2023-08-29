from collections import deque
import sys
input = sys.stdin.readline
def bfs(x) :
    que = deque()
    que.append([x, 0])
    while que :
        x, level = que.popleft()
        
        if level % 2 == 0 :
            if visited[x] == 0 :
                visited[x] = 1
                for i in adj[x] :
                    que.append([i,level+1])
            elif visited[x] == 1 :
                continue
            else :
                return 0
        else :
            if visited[x] == 0 :
                visited[x] = 2
                for i in adj[x] :
                    que.append([i,level+1])
            elif visited[x] == 2 :
                continue
            else :
                return 0
    return 1

T = int(input())
for tc in range(1, T+1) :
    N, M = map(int, input().split())
    adj = [[] for _ in range(N+1)]
    for _ in range(M) :
        s, e = map(int, input().split())
        adj[s].append(e)
        adj[e].append(s)
    visited = [0] * (N+1)
    flag = 1

    for i in range(N) :
        if visited[i] == 0:
            flag = bfs(i)
        if flag == 0 :
            break
    if flag == 0 :
        print('NO')
    else :
        print('YES')