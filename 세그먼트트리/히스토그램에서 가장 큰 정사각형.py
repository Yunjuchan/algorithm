import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
while True :
    arr = list(map(int, input().split()))
    N = arr[0]
    if arr[0] == 0 :
        break
    i = 0
    while True :
        if 2 ** i >= N :
            break
        i += 1

    leaf = 2 ** i - 1
    tree = [21e8] * 2 ** (i+1)
    idx_tree = [j for j in range(2 ** (i+1))]

    for i in range(1,N+1) :
        tree[leaf+i] = arr[i]

    for i in range(leaf, 0, -1) :
        if tree[i*2] > tree[i*2+1] :
            tree[i] = tree[i*2+1]
            idx_tree[i] = idx_tree[i*2+1]
        else :
            tree[i] = tree[i*2]
            idx_tree[i] = idx_tree[i*2]

    def get_idx(a, b) :
        ret = 21e8
        idx = 0
        while a <= b :
            if a % 2 :
                if ret > tree[a] :
                    ret = tree[a]
                    idx = idx_tree[a]
                a += 1
            if not b % 2 :
                if ret > tree[b] :
                    ret = tree[b]
                    idx = idx_tree[b]
                b -= 1
            a //= 2
            b //= 2
        return idx

    def getVal(a, b) :
        if a > b :
            return 0
        idx = get_idx(a, b)
        r1 = (b-a+1) * tree[idx]
        l = idx-1
        r = idx+1
        return max(r1, getVal(a, l), getVal(r, b))

    s, e = leaf+1, leaf+N
    ret = getVal(s, e)
    print(ret)


