
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N, M = map(int, input().split())

visit = [False] * (N+1)
edge = [[] for _ in range(N+1)]
cnt = 0


# 내 풀이
def DFS(v) :
    if visit[v] == True :
        return 0
    stack = []
    visit[v] = True
    for i in range(len(edge[v])) :
        a = edge[v][i]
        if visit[a] == False :
            stack.append(a)
    while stack != [] :
        x = stack.pop() 
        DFS(x)
    return 1
    
for i in range(1, N+1) :
    cnt += DFS(i)
print(cnt)



# 책 풀이
# def DFS(v) :
#     visit[v] = True
#     for i in edge[v] :
#         if not visit[i] :
#             DFS(i)

# for _ in range(M) :
#     u, v = map(int, input().split())
#     edge[u].append(v)
#     edge[v].append(u)

# for i in range(1, N+1) :
#     if not visit[i] :
#         cnt += 1
#         DFS(i)
# print(cnt)
