N = int(input())
A = list(map(int, input().split()))
B = sorted(list(set(A)))
H = {}
for i in range(len(B)) :
    H[B[i]] = i
N2 = len(B)
i = 0 
while True :
    if 2 ** i >= N2 :
        break
    i += 1
leaf = 2 ** i - 1
tree = [0] * 2 ** (i+1)

def update(tree, node, start, end, index, val):
    print(tree)
    if index < start or index > end:
        return
    if start == end:
        tree[node] += val
        return
    update(tree, node*2, start, (start+end)//2, index, val)
    update(tree, node*2+1, (start+end)//2+1, end, index, val)
    tree[node] = tree[node*2] + tree[node*2+1]
        
def query(tree, node, start, end, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    lsum = query(tree, node*2, start, (start+end)//2, left, right)
    rsum = query(tree, node*2+1, (start+end)//2+1, end, left, right)
    return lsum + rsum

result = 0
for i in range(N) :
    l = H[A[i]] + 1
    r = leaf
    result += query(tree, 1, 0, N2-1, l, r)
    print('트리변경')
    update(tree, 0, N2-1, 1, l-1, 1)
print(result)