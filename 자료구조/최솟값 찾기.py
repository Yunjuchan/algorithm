from collections import deque
N, L = map(int, input().split())
D = list(map(int, input().split()))

que = deque()
for i in range(N) :
    while que and que[-1][1] > D[i]:
        que.pop()
    while que and que[0][0] <= i - L:
        que.popleft()
    que.append([i, D[i]])
    print(que[0][1], end=' ')