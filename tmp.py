from collections import deque
N, K = map(int, input().split())
visited = [False] * 100001
def bfs(x, y) :
    que = deque()
    que.append([0, x])
    visited[x] = True
    while que :
        level, now = que.popleft()
        if now == y :
            return level
        n1 = now*2
        if 0 <= n1 <= 100000 and not visited[n1]:
            visited[n1] = True
            que.append([level, n1])
        n2 = now - 1
        if 0 <= n2 <= 100000 and not visited[n2] :
            visited[n2] = True
            que.append([level+1, n2])
        n3 = now + 1
        if 0 <= n3 <= 100000 and not visited[n3] :
            visited[n3] = True
            que.append([level+1, n3])
ret = bfs(N, K)
print(ret)