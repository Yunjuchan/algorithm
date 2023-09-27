from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
pre = [0] * (N+1)
result = {i:{} for i in range(N+1)} 
adj = [[] for _ in range(N+1)]

for _ in range(M) :
    X, Y, K = map(int, input().split())
    pre[X] += 1
    adj[Y].append([X,K])

que = deque()
for x in range(1, N+1) :
    if pre[x] == 0 :
        que.append(x)
        result[x][x] = 1
while que :
    now = que.popleft()
    for next, cnt in adj[now] :
        pre[next] -= 1
        for k, v in result[now].items() :
                result[next][k] = result[next].get(k,0) + v*cnt
        if pre[next] == 0 :
            que.append(next)  
          
            
A = sorted(list(result[N].items()))        
for a, b in A :
     print(a, b)