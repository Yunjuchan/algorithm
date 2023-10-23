N = int(input())
dice = [input() for _ in range(N)]
visited = [False] * N
path = [-1]*N
value = [-1]*N
Min = 21e8
Max = -21e8
def is_cycle(i, j, level) :
    if i == path[j] :
        return level
    return is_cycle(i, path[j], level+1)
        
def dfs(level, path, value) :
    global Min, Max
    if level == N :
        mul = 1
        cycle = [0]*N
        for i in range(N) :
            tmp = 0
            cycle[is_cycle(i, i, 0)] += 1
        for i in range(N) :
            tmp += cycle[i] // (i+1)
        if  not tmp % 2 :
            mul *= -1
        for x in value :
            mul *= x
        if Min > mul :
            Min = mul
        if Max < mul :
            Max = mul
        return
    
    for i in range(N) :
        if visited[i] == True : continue
        visited[i] = True
        path[level] = i
        if dice[level][i].isdigit() :
            value[level] = int(dice[level][i])
        else :
            value[level] = -(ord(dice[level][i])-64)
        dfs(level+1, path, value)
        value[level] = 0
        path[level] = -1
        visited[i] = False

dfs(0, path, value)
print(Min)
print(Max)
