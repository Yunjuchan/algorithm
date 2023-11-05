from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
P = [0] + list(map(int, input().split()))
visited = [False] * (N+1)
total = sum(P)
result = total
adj = [[]]
lst = []
for _ in range(N) :
    n, *x = map(int, input().split())
    adj.append(x)

def check(x, y) :
    visited2 = [False] * (N+1)
    que = deque()
    que.append(x)
    visited2[x] = True
    while que :
        now = que.popleft()
        for i in adj[now] :
            if visited2[i] or visited[i] : continue
            visited2[i] = True
            que.append(i)
    que.append(y)
    visited2[y] = True 
    while que :
        now = que.popleft()
        for i in adj[now] :
            if visited2[i] or not visited[i] : continue
            visited2[i] = True
            que.append(i)
    return sum(visited2)


def dfs(start, Sum) :
    global result
    if Sum == total : return
    if Sum != 0 :
        for i in range(1, N+1) :
            if visited[i] : continue
            ret = check(i, start-1)
            break
        if ret == N :
            if result > abs(total - 2*Sum) :
                result = abs(total - 2*Sum)

    for i in range(start, N+1) :
        visited[i] = True
        dfs(i+1, Sum + P[i])
        visited[i] = False

dfs(0, 0)
if result == total :
    print(-1)
else :
    print(result)


