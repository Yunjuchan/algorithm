import sys
input = sys.stdin.readline
V, E = map(int, input().split())
edge_list = [[] for _ in range(V)] 
visited = [False] * V
arrive = False

for _ in range(E) :
    s, e = map(int, input().split())
    edge_list[s].append(e)
    edge_list[e].append(s)

def DFS(v, chain) :
    global arrive
    if chain == 4:
        arrive = True
        return
    visited[v] = True
    for i in edge_list[v] :
        if visited[i]  == False :
            DFS(i, chain+1)
    visited[v] = False



for i in range(V) :   
    DFS(i,0)
    if arrive :
        break
if arrive :
    print(1)
else :
    print(0)




