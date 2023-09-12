import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def find(x) :
    if top[x][0] == -1 :
        return x
    ret = find(top[x][0])
    top[x][0] = ret
    return ret

def union(a, b, d) :
    if a > b :
        a, b = b, a
    fa, fb = map(find, [a, b])
    if fa == fb :
        return
    top[fb] = [fa, d] 

N = int(input())
INF = 21e8
top = [[-1, INF]] * N
L = []
for i in range(N) :
    L.append([i, *map(int, input().split())])

L.sort(key=lambda x : (x[1], x[0]))
for i in range(N-1) :
    if top[i+1][1] > abs(L[i][1] - L[i+1][1]) :
        # top[i+1] = [-1, INF]
        union(L[i][0], L[i+1][0], abs(L[i][1] - L[i+1][1]))

L.sort(key=lambda x : x[2])
for i in range(N-1) :
    if top[i+1][1] > abs(L[i][2] - L[i+1][2]) :
        # top[i+1] = [-1, INF]
        union(L[i][0], L[i+1][0], abs(L[i][2] - L[i+1][2]))

L.sort(key=lambda x : x[3])
for i in range(N-1) :
    if top[i+1][1] > abs(L[i][3] - L[i+1][3]) :
        # top[i+1] = [-1, INF]
        union(L[i][0], L[i+1][0], abs(L[i][3] - L[i+1][3]))

result = 0
for i in range(N) :
    if top[i][1] != INF :
        result += top[i][1]
print(result)