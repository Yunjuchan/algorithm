from collections import deque
T = int(input())
for tc in range(1, T+1) :
    N, K = map(int, input().split())
    lst = [0]*(N+1)
    result = [0]*(N+1)
    adj = [[] for _ in range(N+1)]
    time = list(map(int, input().split()))
    time = [0] + time
    for _ in range(K) :
        s, e= map(int, input().split())
        adj[s].append(e)
        lst[e] += 1
    que = deque()
    for i in range(1, N+1) :
        if lst[i] == 0 :
            que.append(i)
    
    while que :
        now = que.popleft()
        for x in adj[now] :
            lst[x] -= 1
            if result[now] + time[now] > result[x] :
                result[x] = result[now] + time[now] 
            if lst[x] == 0 :
                que.append(x)
    
    end = int(input())
    print(result[end]+time[end])

