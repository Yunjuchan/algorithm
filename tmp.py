import sys
sys.setrecursionlimit(100000)
def dfs(x):
    for i in lst[x]:
        if visited[i]==0:
            visited[i] = 1
            par[i] = x
            dfs(i)
            
n = int(input())
lst= [[] for _ in range(n+1)]
for i in range(1,n):
    s,e = map(int,input().split())
    lst[s].append(e)
    lst[e].append(s)
par = [0]*(n+1)    
# for i in range(2,n+1):
visited = [0]*(n+1)
visited[1]=1
result=[]
dfs(1)
for i in par[2:]:
    print(i)
