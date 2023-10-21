def changeTree(s) :
    s += leaf+1
    
N = int(input())
A = list(map(int, input().split()))
B = sorted(A)
B2 = sorted(list(set(A)))
H = {}
for i in range(N) :
    H[B[i]] = H.get(B[i], 0) + 1
print(B)
print(H)
i = 0 
while True :
    if 2 ** i >= N :
        break
    i += 1
leaf = 2 ** i - 1
tree = [0] * 2 ** (i+1)

def changeTree(s, e, node, i) :
    if i < s or i > e :
        return 0
    tree[node] += 1
    if s != e :
        changeTree(s, (s+e)//2, node*2, i)
        changeTree((s+e)//2+1, e, node*2+1, i)

def calc(s, e, node, l, r) :
    if e < l or r < s :
        return 0
    
    if l <= s and e <= r :
        return tree[node]
    
    lsum = calc(s, (s+e)//2, node*2, l, r)
    rsum = calc((s+e)//2+1, e, node*2+1, l, r)
    return lsum+rsum

result = 0
for i in range(N) :
    pass
print(result)