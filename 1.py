N, M = map(int, input().split())
path = []
visited = [False] * (N+1)
def abc(level) :
    if level == M :
        print(*path)
        return
    for i in range(1,N+1) :
        if not visited[i] :
            visited[i] = True
            path.append(i)
            abc(level+1)
            visited[i] = False
            path.pop()
abc(0)