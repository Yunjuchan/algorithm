import sys
sys.setrecursionlimit(10**7)

x = input()
N = len(x)
visited = [False] * N
lst = [0]*26
dp = [i for i in range(N+1)] 
dp[0] = 1

for i in range(1, N+1) :
    dp[i] *= dp[i-1]

def dfs(level, path) :
    global cnt
    if level == N :
        cnt += 1
        return
    
    for i in range(N) :
        if not visited[i] and path[-1] != x[i]:
            visited[i] = True
            dfs(level+1, path+x[i])
            visited[i] = False

cnt = 0
for i in range(N) :
    lst[ord(x[i])-97] += 1
    visited[i] = True
    dfs(1, x[i])
    visited[i] = False

for i in range(26) : 
    cnt //= dp[lst[i]]
print(cnt)

