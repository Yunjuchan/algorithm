import sys
input = sys.stdin.readline
N = int(input())
mat_list = []
for _ in range(N) :
    mat_list.append(list(map(int, input().split())))
D = [0]*(N+1)
D[0] = mat_list[0][0]
for i in range(1,N+1) :
    D[i] = mat_list[i-1][1]
INF = 21e8
dp = [[INF]*N for _ in range(N)]
for i in range(N) :
    dp[i][i] = 0
for i in range(1, N) :      # 부분 행렬의 길이
    for j in range(N-i) :   # 행 번호
        n = j+i
        for k in range(j, n) :    
            temp = dp[j][k] + dp[k+1][n] + D[j]*D[k+1]*D[n+1]
            if temp < dp[j][n] :
                dp[j][n] = temp          
print(dp[0][N-1])
# for a in dp :
#     print(*a)
