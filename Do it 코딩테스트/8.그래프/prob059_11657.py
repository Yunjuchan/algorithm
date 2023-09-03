from collections import deque
N, M = map(int, input().split())
edge = []
INF = 21e8
D = [INF] * (N+1)
D[1] = 0
for _ in range(M) :
    edge.append(list(map(int, input().split())))
flag = 0
for i in range(N-1) :
    for s, e, w in edge :
        if D[s] == INF : continue
        if D[e] > D[s] + w :
            D[e] = D[s] + w
for s, e, w in edge :
    if D[s] == INF : continue
    if D[e] > D[s] + w :
        flag = 1 
        break
if flag == 1 :
    print(-1)
else :
    for i in D[2:] :
        if i != INF :
            print(i)
        else :
            print(-1)
