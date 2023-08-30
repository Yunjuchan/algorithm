import sys
input = sys.stdin.readline

def union(a, b) :
    fa, fb = map(find, [a, b])
    if fa == fb  :
        return
    top[fb] = fa

def find(x) :
    if top[x] == -1 :
        return x
    ret = find(top[x])
    top[x] = ret
    return ret

N = int(input())
M = int(input())
top = [-1] * (N+1)
adj = [list(map(int, input().split())) for _ in range(N)]
trip = list(map(int, input().split()))

for i in range(N) :
    for j in range(i+1, N) :
        if adj[i][j] == 1 :
            union(i+1, j+1)
flag = 1
for i in range(M-1) :
    if find(trip[i]) != find(trip[i+1]) :
        flag = 0
        break
if flag == 1 :
    print('YES')
else :
    print('NO')