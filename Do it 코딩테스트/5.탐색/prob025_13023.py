import sys
input = sys.stdin.readline
V, E = map(int, input().split())
edge_list = [[]] * V
visited = [False] * V
arrive = False

def DFS(v, chain) :
    global arrive
    if chain == 4:
        arrive = True
        return
    
    

    for i in edge_list[v] :
        if not visited[i] :
            visited[v] = True
            DFS(i, chain+1)
            visited[v] = False

for _ in range(E) :
    s, e = map(int, input().split())
    edge_list[s].append(e)
    edge_list[e].append(s)

for i in range(V) :   
    DFS(i,0)
    visited[i] = False
    if arrive :
        break
if arrive :
    print(1)
else :
    print(0)


