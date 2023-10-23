import sys
input = sys.stdin.readline
N = int(input().rstrip())
A = list(map(int, input().split()))
i = 0
while 2 ** i < N :
    i += 1
last_ans = 0
leaf = 2 ** i - 1
tree = [0] * 2 ** (i+1)

for i in range(N) :
    tree[leaf+i+1] = A[i]
print(tree)

M = int(input().rstrip())
for _ in range(M) :
    input()