def Min(a, b) :
    ret = INF
    s = leaf+a
    e = leaf+b
    while s <= e :
        if s % 2 :
            if ret > Mintree[s] :
                ret = Mintree[s]
        s += 1
        if not e % 2 :
            if ret > Mintree[e] :
                ret = Mintree[e]
        e -= 1
        s //= 2
        e //= 2
    return ret            
def Max(a, b) :
    ret = 0
    s = leaf+a
    e = leaf+b
    while s <= e :
        if s % 2 :
            if ret < Maxtree[s] :
                ret = Maxtree[s]
        s += 1
        if not e % 2 :
            if ret < Maxtree[e] :
                ret = Maxtree[e]
        e -= 1
        s //= 2
        e //= 2
    return ret  


import sys
input = sys.stdin.readline
N, M = map(int, input().split())
INF = 21e8

i = 0
while True :
    if 2 ** i >= N :
        break
    i += 1

leaf = 2 ** i - 1
Mintree = [INF] * 2 ** (i+1)
Maxtree = [0] * 2 ** (i+1)

for i in range(1, N+1) :
    x = int(input().rstrip())
    Mintree[leaf+i] = x
    Maxtree[leaf+i] = x

for i in range(leaf, 0, -1) :
    Mintree[i] = min(Mintree[i*2], Mintree[i*2+1])
    Maxtree[i] = max(Maxtree[i*2], Maxtree[i*2+1])

for _ in range(M) :
    a, b = map(int, input().split())
    ret1 = Min(a, b)
    ret2 = Max(a, b)
    print(ret1, ret2)
