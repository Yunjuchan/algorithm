from heapq import heappush, heappop
while True :
    N, M = map(int, input().split())
    if N == M == 0 : break
    s, e = map(int, input().split())
    adj = [[] for _ in range(N)]
    INF = 21e8
    
    visited = [[False]*N for _ in range(N)]
    visited2 = [[False]*N for _ in range(N)]
    que = []
    result = []
    for _ in range(M) :
        u, v, d = map(int, input().split())
        adj[u].append((v, d))

    dist = [INF] * N 
    dist[s] = 0
    result_visited = [False] * len(adj[s])
    for i in range(len(adj[s])) :
        heappush(que, [adj[s][i][1], s, adj[s][i][0], i, []])
        dist[adj[s][i][0]] = adj[s][i][1]
    
    Min = 21e8
    while que :
        d, pre, now, tp, path = heappop(que)
        path.append([pre, now])
        print(path)
        print(tp)
        if visited[pre][now] : continue
        if now == e :
            if Min >= d :
                result_visited[tp] = True
                Min = d
                for s, e in path :
                    visited2[s][e] = True
                continue
            else :
                break
        if result_visited[tp] : continue
        visited[pre][now] = True
        for next, next_d in adj[now] :
            if visited[now][next] : continue
            if dist[next] > d + next_d :
                visited[now][next] = True
                dist[next] = d + next_d
                heappush(que, [dist[next], now, next, tp, path])
    print(result_visited)
    
    


