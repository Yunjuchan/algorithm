from collections import deque
import sys
input = sys.stdin.readline
N = int(input().rstrip())
P = input().split()
P.sort()
M = int(input().rstrip())
adj = {}
des = {}
top = {}
for p in P :
    adj[p] = []
    top[p] = 0
    des[p] = []
for _ in range(M) :
    x, y = input().split()
    adj[y] = adj.get(y, []) + [x]
    top[x] = top.get(x, 0) + 1
for p in adj :
    adj[p].sort()
root = deque()
for p in P :
    if top[p] == 0 :
        root.append(p)
print(len(root))
print(*root)
while root :
    now = root.popleft()
    for next in adj[now] :
        top[next] -= 1
        if top[next] == 0 :
            des[now].append(next)
            root.append(next)
for p in P :
    print(p, len(des[p]), *des[p])