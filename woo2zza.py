import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
N = int(input())
adj = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    s, e, w = map(int, input().split())
    adj[s].append([e, w])
W = [0] * (N + 1)


def dfs(now, Sum):
    global Max
    W[now] = Sum
    x = W[now]

    for next, w in adj[now]:
        dfs(next, Sum + w)
        if W[next] > x:
            x = W[next]

    if len(adj[now]) >= 2:
        tmp = [0] * len(adj[now])
        for i in range(len(adj[now])):
            tmp[i] = W[adj[now][i][0]] - W[now]
        tmp.sort()
        result = abs(tmp[-1] + tmp[-2])
        if result > Max:
            Max = result
            
    W[now] = x

Max = 0
dfs(1, 0)
print(max(Max, W[1]))