import sys
input = sys.stdin.readline

def update_lazy(node, s, e) :
    if lazy[node] :
        tree[node] = (e - s + 1) - tree[node]
        
        if s != e :
            lazy[node*2] ^= 1
            lazy[node*2+1] ^= 1

        lazy[node] = 0

def changeTree(node, s, e, l, r) :
    update_lazy(node, s, e)
    if l > e or r < s :
        return    
    if l <= s and e <= r:
        tree[node] = (e - s + 1) - tree[node]

        if s != e:
            lazy[node*2] ^= 1
            lazy[node*2+1] ^= 1
        return
    changeTree(node*2, s, (s+e)//2, l, r)
    changeTree(node*2+1, (s+e)//2+1, e, l, r)
    tree[node] = tree[node*2] + tree[node*2+1] 

def query(node, s, e, l, r) :
    update_lazy(node, s, e)
    if l > e or s > r : return 0
    if l <= s and e <= r :
        return tree[node]
    lsum = query(node*2, s, (s+e)//2, l, r)
    rsum = query(node*2+1, (s+e)//2+1, e, l, r)
    return lsum+rsum

N, M = map(int, input().split())
i = 0
while 2 ** i < N :
    i += 1
leaf = 2 ** i - 1
tree = [0] * 2 ** (i+1)
lazy = [0] * 2 ** (i+1)

for _ in range(M) :
    x, a, b = map(int, input().split())
    if x == 0 :
        changeTree(1, 0, N-1, a-1, b-1)
    else :
        print(query(1, 0, N-1, a-1, b-1))

