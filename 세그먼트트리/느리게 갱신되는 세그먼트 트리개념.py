# 느리게 갱신되는 세그먼트트리는 구간의 값이 변화될 때 사용한다.
# 일반적인 세그먼트트리는 1번만 변화하면 되기 때문에 
# 바뀐 값을 이용해 세그먼트트리를 즉시 갱신한다.
# 하지만 구간이 변화하는 세그먼트트리는 구간의 길이만큼 반복해줘야하기 때문에 시간복잡도가 높아진다.
# 이 문제를 해결하기 위해 lazy라는 배열을 생성하였다.

# 갱신이 필요한 노드들을 먼저 계산해주고 리프노드는 마지막에 갱신해준다는 개념 아직 이해 부족

# 느리게 갱신되는 세그먼트 트리는 탑다운 방식으로 진행하는 재귀형태이다.
# 각 함수에 들어있는 node의 값은 부모노드를 뜻한다. 
# 가장 첫번째 부모는 루트노드이고 기존까지 세그먼트 트리에서 루트노드는 1번이었다. 
# 느리게 갱신되는 세그먼트 트리의 루트도 1번으로 동일하게 사용할 것이다.

# 먼저 lazy를 갱신하는 함수이다.
# lazy의 부모의 lazy값이 0이 아닐때 즉 갱신할 값이 있으면 tree는 lazy값을 이용해 tree를 갱신해준다.
# 또한 자식의 lazy에 값을 전달해준다.
def update_lazy(node, start, end):
    if lazy[node] != 0: 
        tree[node] += (end-start+1)*lazy[node]  
        if start != end:
            lazy[node*2] += lazy[node]
            lazy[node*2+1] += lazy[node]
        lazy[node] = 0

# 찾아야하는 범위에서 갱신해야하는 노드를 찾고 값을 갱신하는 기능을 가지고 있으며
# 재귀를 통해 탐색한다. 
# 초기 node는 가장 큰 부모인 조상노드, start와 end는 찾아야할 범위의 양끝인덱스를 적어준다. 
# left와 right는 갱신할 범위를 적어준다.
# diff는 변화량을 적어준다.
def update_range(node, start, end, left, right, diff):
    update_lazy(node, start, end)
    if left > end or right < start: # 갱신할 범위가 찾아야할 범위를 넘어섰을때는 찾지 못함
        return  
    if left <= start and end <= right: # 찾아야할 범위가 갱신할 범위안에 포함되어 있어야함
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

import sys
import math
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n, m, k = map(int, input().split())

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
for i in range(1,n+1) :
    tree[leaf+i] = int(input().rstrip())
# 자식노드들의 합을 더해 세그먼트 트리를 갱신
for i in range(leaf, 0, -1) :
    tree[i] += tree[i*2] + tree[i*2+1]
for _ in range(m+k):
    what, *q = map(int, input().split())
    if what == 1:
        left, right, diff = q
        update_range(1, 0, leaf, left-1, right-1, diff)
        print('update 실행') 
        print('tree changed : ', tree)
        print('lazy changed : ', lazy)
    else:
        left, right = q
        print(query(1, 0, leaf, left-1, right-1))
        print('query 실행')
        print('tree changed : ', tree)
        print('lazy changed : ', lazy)
        

