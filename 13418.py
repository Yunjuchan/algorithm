import sys
input = sys.stdin.readline
def find(x) :
    if top[x] == -1 :
        return x
    ret = find(top[x])
    top[x] = ret
    return ret

def union(a, b, w) :
    global ret
    fa, fb = map(find, [a, b])
    if fa == fb :
        return
    top[fb] = fa
    ret += (w+1)%2
    return
    
    
N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]

for _ in range(M+1) :
    s, e, w = map(int, input().split())
    adj[s].append([e,w])
ret = 0
top = [-1] * (N+1)
for i in range(N+1) :
    for j, w in adj[i] :
        if w == 0 :
            union(i, j, w)

for i in range(N+1) :
    for j, w in adj[i] :
        if w == 1 :
            union(i, j, w)
ret1 = ret
ret = 0
top = [-1] * (N+1)
for i in range(N+1) :
    for j, w in adj[i] :
        if w == 1 :
            union(i, j, w)

for i in range(N+1) :
    for j, w in adj[i] :
        if w == 0 :
            union(i, j, w)

print(ret1**2 - ret**2)

