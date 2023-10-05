from collections import deque
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
n = 6
def solution(n, edge):
    answer = 0
    result_level = 0
    que = deque()
    que.append([1,0])
    visited = [False] *(n+1)
    visited[1] = True
    adj = [[] for _ in range(n+1)]
    for s, e in edge :
        adj[s].append(e)
        adj[e].append(s)
    while que :
        now, level = que.popleft()
        if result_level == level :
            answer += 1
        else :
            result_level = level
            answer = 1
        for next in adj[now] :
            if not visited[next] :
                visited[next] = True
                que.append([next, level+1]) 
    return answer
print(solution(n, vertex))