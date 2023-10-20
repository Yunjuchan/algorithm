import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
i = 0

while True :
    if 2 ** i >= N :
        break
    i += 1
leaf = 2 ** i - 1
tree = [0] * 2 ** (i+1)
for i in range(N) :
    tree[leaf+i+1] = arr[i]

for i in range(leaf, 0, -1) :
    tree[i] = tree[i*2] + tree[i*2+1]

def changeTree(a, b) :
    a += leaf
    d = b - tree[a]
    while a > 0 :
        tree[a] += d
        a //= 2

def query(a, b) :
    if a > b :
        a, b = b, a
    ret = 0
    s = a + leaf    
    e = b + leaf
    while s <= e :
        if s % 2 :
            ret += tree[s]
            s += 1
        if not e % 2 :
            ret += tree[e] 
            e -= 1
        s //= 2
        e //= 2
    return ret 


for _ in range(M) :
    a, b, c, d = map(int, input().split())
    print(query(a, b))
    changeTree(c, d)

#fdsfsda