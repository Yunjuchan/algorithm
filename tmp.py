N, K = map(int, input().split())
dp = [i for i in range(11)]
dp[0] = 1
for i in range(2, 11) :
    dp[i] *= dp[i-1]
print(dp[N]//(dp[K]*dp[N-K]))