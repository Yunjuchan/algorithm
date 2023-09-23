N = int(input())
candies = []
for _ in range(N) :
    candies.append(int(input()))
candies.sort()
dp = [[0]*(sum(candies)+1) for _ in range(N+1)] 
cnt = [0] * (sum(candies)+1)
for i in range(1, N+1) :
    for j in range(1, sum(candies)+1) :
        w = candies[i-1]
        if j == w :
            dp[i][j] = 1
        if dp[i-1][j-w] != 0 :
            dp[i][j] = 1
for a in dp :
    print(*a)
