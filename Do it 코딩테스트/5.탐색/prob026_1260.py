import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10000)
N, M, V = map(int, input().split())

adjacant = [[] for _ in range(N+1)] 
for i in range(M) :
    a, b = map(int, input().split())
    adjacant[a].append(b)
    adjacant[b].append(a)

for i in range(1,N+1) :
    adjacant[i].sort()
    adjacant[i] = deque(adjacant[i])

dfs_path = []
def DFS(x) :
    if x not in dfs_path :
        dfs_path.append(x)
        for i in range(len(adjacant[x])) :
            DFS(adjacant[x][i])      
        return

DFS(V)
print(*dfs_path)

bfs_path = []
que = deque([])
def BFS(x) :
    if x not in bfs_path :
        bfs_path.append(x)
        while adjacant[x] != deque([]) :
            que.append(adjacant[x].popleft())
        while que != deque([]) :
            BFS(que.popleft())
        return
BFS(V)
print(*bfs_path)

