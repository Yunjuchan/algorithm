from collections import deque
def bfs(x, n, computers) :
    que = deque()
    que.append(x)
    while que :
        now = que.popleft()
        for next in range(n) :
            if not visited[next] and computers[now][next] == 1 :
                visited[next] = True
                que.append(next)
                
def solution(n, computers):
    global visited
    answer = 0
    visited = [False]*n
    for i in range(n) :
        if not visited[i] :
            visited[i] = True
            bfs(i, n, computers)
            answer += 1    
    return answer
n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
ret = solution(n, computers)
print(ret)