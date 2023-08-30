import sys
input = sys.stdin.readline
N, M = map(int, input().split())
top = [-1] * (N+1)
def find(x) :
    if top[x] == -1 :
        return x
    ret = find(top[x])
    top[x] = ret
    return ret

def union(a, b) :
    fa, fb = map(find, [a, b])
    if fa == fb :
        return
    top[fb] = fa

for _ in range(M) :
    x, a, b = map(int, input().split())
    if x == 0 :
        union(a, b)
    else :
        if find(a) == find(b) :
            print('YES')
        else :
            print('NO')