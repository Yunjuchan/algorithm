import sys
sys.setrecursionlimit(10**6)
N = int(input())
eggs = []
for _ in range(N) :
    eggs.append(list(map(int, input().split())))
visited = [False] * N
Max = 0
def dfs(n, level) :
    global Max
    if n > Max :
        Max = n

    if n == N :
        Max = N 
        return
    elif level == N :
        return
    elif level == n == N - 1 :
        if n > Max :
            Max = n
            return
    
    if visited[level] :
        dfs(n, level+1)
        return

    
    for i in range(N) :
        if i == level or visited[i] : continue
        
        if eggs[level][1] >= eggs[i][0] and eggs[i][1] >= eggs[level][0] :
            visited[level] = True
            visited[i] = True
            dfs(n+2, level+1)
            visited[level] = False
            visited[i] = False
        
        elif eggs[level][1] >= eggs[i][0] :
            visited[i] = True
            eggs[level][0] -= eggs[i][1]
            dfs(n+1, level+1)
            eggs[level][0] += eggs[i][1]
            visited[i] = False
        
        elif eggs[i][1] >= eggs[level][0] :
            visited[level] = True
            eggs[i][0] -= eggs[level][1]
            dfs(n+1, level+1)
            eggs[i][0] += eggs[level][1]
            visited[level] = False
        
        else :
            eggs[i][0] -= eggs[level][1]
            eggs[level][0] -= eggs[i][1]
            dfs(n, level+1)
            eggs[i][0] += eggs[level][1]
            eggs[level][0] += eggs[i][1]
dfs(0,0)
print(Max)
        



