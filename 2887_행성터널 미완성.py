import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def find(x) :
    if top[x] == -1 :
        return x
    ret = find(top[x])
    top[x] = ret
    return ret

def union(a, b, d) :
    global result
    fa, fb = map(find, [a, b])
    if fa == fb :
        return
    top[fb] = fa
    result += d


N = int(input())
INF = 21e8
top = [-1] * N

L = []
L2 = []
for i in range(N) :
    L.append([i, *map(int, input().split())])
L.sort(key=lambda x : (x[1], x[0]))
for i in range(N-1) :
    L2.append([L[i+1][1] - L[i][1], L[i][0], L[i+1][0]])
    

L.sort(key=lambda x : x[2])
for i in range(N-1) :
        L2.append([L[i+1][2] - L[i][2], L[i][0], L[i+1][0]])
L.sort(key=lambda x : x[3])
for i in range(N-1) :
        L2.append([L[i+1][3] - L[i][3], L[i][0], L[i+1][0]])
L2.sort()
result = 0
for d, i, j in L2 :
    union(i, j ,d)
    
print(result)
