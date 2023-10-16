T = int(input())
for tc in range(1, T+1) :
    N = int(input())
    A = list(map(int, input().split()))
    visited = [False] * N
    def dfs(level, score) :
        global Max
        if level == N :
            if score > Max :
                Max = score 
            return
        left = right = -1
        for i in range(N) :
            if visited[i] : continue
            visited[i] = True
            left = right = -1
            for j in range(i-1, -1, -1) :
                if i == 0 : break
                if not visited[j] :
                    left = A[j]
                    break
            for j in range(i+1, N) :
                if i == N-1 : break
                if not visited[j] :
                    right = A[j]
                    break
            if right == left == -1 :
                dfs(level+1, score+A[i])
            elif right != -1 and left != -1 :
                dfs(level+1, score+right*left)
            else :
                dfs(level+1, score+abs(right*left))
            visited[i] = False
    Max = 0
    dfs(0,0)
    print(f'#{tc} {Max}')

 
