import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def dfs(x) :
    for i in adj[x]     :
        if not visited[i] :
            visited[i] = True
            dfs(i)
N, M, k = map(int, input().split())
lst = list(enumerate(map(int, input().split())))
adj = [set([i]) for i in range(N+1)]
visited = [False]*(N+1)
visited[0] = True
lst.sort(key=lambda x : x[1])
for _ in range(M) :
    s, e = map(int, input().split())
    adj[s].add(e)
    adj[e].add(s)
total = 0
for i, p in lst :
    if k-p < 0 : break
    if not visited[i+1] :
        k -= p
        total += p
        dfs(i+1)
if sum(visited) == N+1 :
    print(total)
else :
    print('Oh no')
    
