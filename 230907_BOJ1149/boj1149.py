import sys
input = sys.stdin.readline
N = int(input())
INF = 21e8
dp = [[INF,INF,INF] for _ in range(N)]
rgb = []
for _ in range(N) :
    rgb.append(list(map(int, input().split()))) # rgb
dp[0] = rgb[0]
for i in range(1, N) :
    for j in range(3) :
        for k in range(3) :
            if j == k : continue
            dp[i][k] = min(dp[i][k], dp[i-1][j]+rgb[i][k])
print(min(dp[N-1]))