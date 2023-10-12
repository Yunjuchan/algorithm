import sys
input = sys.stdin.readline
N, S, M = map(int, input().split())
V = list(map(int, input().split()))
dp = [-1] * (N+1)
dp[0] = S
for i in range(N) :
    dp[i+1] = dp[i] + V[i]
    dp[i+1] = dp[i] - V[i]



