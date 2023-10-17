import sys
input = sys.stdin.readline

def changeTree(x, y) :
    idx = x+leaf
    tree[idx] = y
    while idx > 1 : 
        tree[idx//2] = tree[(idx//2)*2] % 1000000007 * tree[(idx//2)*2+1] % 1000000007
        idx //= 2


def calc(a, b) :
    ret = 1
    s, e = a+leaf, b+leaf
    while s <= e :
        if s % 2 :
            ret *= tree[s] % 1000000007
            s += 1
        if not e % 2 :
            ret *= tree[e] % 1000000007
            e -= 1
        s //= 2
        e //= 2
    return ret


N, M ,K = map(int, input().split())
i = 0
while True :
    if 2 ** i >= N :
        break
    i += 1
leaf = 2 ** i - 1
tree = [1] * 2**(i+1)
for i in range(1,N+1) :
    tree[leaf+i] = int(input().rstrip())
for i in range(leaf+N, 1, -1) :
    tree[i//2] *= tree[i] % 1000000007

for _ in range(M+K) :
    x, a, b = map(int, input().split())
    if x == 1 :
        changeTree(a, b)
    else :
        ret = calc(a, b)
        print(ret)