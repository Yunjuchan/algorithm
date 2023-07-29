### 어려움 stack 구현 / 인덱스를 불러오는 것

import sys
input = sys.stdin.readline
N = int(input())
lst = list(map(int, input().split()))
stack = []
nge = [-1] * 4
for i in range(len(lst)) :
    stack.append(i)
    # while/

