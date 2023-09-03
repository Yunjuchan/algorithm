from collections import deque


N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]
lst = [0] * (N+1)
for _ in range(M) :
    s, e = map(int, input().split())
    adj[s].append(e)
    lst[e] += 1
que = deque()
for i in range(1,N+1) :
    if lst[i] == 0 :
        que.append([i, 1])
cnt_list = [0] * (N+1)

while que :
    now, cnt = que.popleft()
    cnt_list[now] = cnt
    for next in adj[now] :
        lst[next] -= 1
        if lst[next] == 0 :
            que.append([next, cnt+1])
print(*cnt_list[1:])