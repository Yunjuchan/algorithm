from collections import deque
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T) :

    K, M, P = map(int, input().split())
    adj = [[] for _ in range(M+1)]
    lst = [0]*(M+1)
    stra = [[0,0] for _ in range(M+1)]
    for _ in range(P) :
        s, e = map(int, input().split())
        adj[s].append(e)
        lst[e] += 1
    que = deque()
    
    for i in range(1, M+1) :
        if lst[i] == 0 :
            stra[i] = [1,1]
            que.append([i, 1])
    
    while que :
        now, level = que.popleft()
        
        for i in adj[now] :
            lst[i] -= 1
            if stra[i][0] < level :
                stra[i] = [level,1]
            elif stra[i][0] == level :
                stra[i][1] += 1
            
            if lst[i] == 0 :
                if stra[i][1] == 1 :
                    que.append([i, stra[i][0]])
                else :
                    que.append([i, stra[i][0]+1])
    result = stra[M][0]
    if stra[M][1] != 1 :
        result += 1
    print(K, result)
