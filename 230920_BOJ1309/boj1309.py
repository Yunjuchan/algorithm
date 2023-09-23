N = int(input())
dp = [0] * (N+1)
dp[0] = 1
dp[1] = 1 + 2
for k in range(2, N+1):
    dp[k] = (dp[k-1]*2+dp[k-2]) % 9901
print(dp[N])