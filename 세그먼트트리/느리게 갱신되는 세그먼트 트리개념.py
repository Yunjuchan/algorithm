# # 합에 대해서 알아보자
# arr = [5,4,3,2,1,2,5]
# N = len(arr)

# # 세그먼트트리 생성
# # 원래 배열을 리프노드에 넣어준다.
# # 따라서 리프노드의 개수는 N보다 많아야한다.
# i = 0
# while True :
#     if 2 ** i >= N :
#         break
#     i += 1

# leaf = 2 ** i - 1   # 리프노드의 시작번호의 전을 저장해준다.

# tree = [0] * 2 * (i+1)
# lazy = tree[:]
# for i in range(N) :
#     tree[leaf+i+1] = arr[i]

# # 자식노드들의 합을 더해 세그먼트 트리를 갱신
# for i in range(leaf, 0, -1) :
#     tree[i] += tree[i*2] + tree[i*2+1]

# 느리게 갱신되는 세그먼트트리는 구간의 값이 변화될 때 사용한다.
# 일반적인 세그먼트트리는 1번만 변화하면 되기 때문에 
# 바뀐 값을 이용해 세그먼트트리를 즉시 갱신한다.
# 하지만 구간이 변화하는 세그먼트트리는 구간의 길이만큼 반복해줘야하기 때문에 시간복잡도가 높아진다.
# 이 문제를 해결하기 위해 lazy라는 배열을 생성하였다.

# 갱신이 필요한 노드들을 먼저 계산해주고 리프노드는 마지막에 갱신해준다는 개념 아직 이해 부족
def update_lazy(node, start, end):
    if lazy[node] != 0:
        tree[node] += (end-start+1)*lazy[node]
        if start != end:
            lazy[node*2] += lazy[node]
            lazy[node*2+1] += lazy[node]
        lazy[node] = 0

def update_range(node, start, end, left, right, diff):
    update_lazy(node, start, end)
    if left > end or right < start:
        return
    if left <= start and end <= right:
        tree[node] += (end-start+1)*diff
        if start != end:
            lazy[node*2] += diff
            lazy[node*2+1] += diff
        return
    update_range(node*2, start, (start+end)//2, left, right, diff)
    update_range(node*2+1, (start+end)//2+1, end, left, right, diff)
    tree[node] = tree[node*2] + tree[node*2+1]


def query(node, start, end, left, right):
    update_lazy(node, start, end)
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    lsum = query(node*2, start, (start+end)//2, left, right)
    rsum = query(node*2+1, (start+end)//2+1, end, left, right)
    return lsum + rsum

import math
n, m, k = map(int, input().split())
a = [int(input()) for _ in range(n)]

# 세그먼트트리 생성
# 원래 배열을 리프노드에 넣어준다.
# 따라서 리프노드의 개수는 N보다 많아야한다.
i = 0
while True :
    if 2 ** i >= n :
        break
    i += 1
leaf = 2 ** i - 1   # 리프노드의 시작번호의 전을 저장해준다.

tree = [0] * 2 ** (i+1)
lazy = tree[:]
for i in range(n) :
    tree[leaf+i+1] = a[i]

# 자식노드들의 합을 더해 세그먼트 트리를 갱신
for i in range(leaf, 0, -1) :
    tree[i] += tree[i*2] + tree[i*2+1]
print(tree)
for _ in range(m+k):
    what, *q = map(int, input().split())
    if what == 1:
        left, right, diff = q
        update_range(1, 0, n-1, left-1, right-1, diff)
    else:
        left, right = q
        print(query(1, 0, n-1, left-1, right-1))

