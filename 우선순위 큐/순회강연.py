from heapq import heappush, heappop
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N = int(input().rstrip())
visited = [False] * 10001
que = []
result = 0

for _ in range(N) :
    p, d = map(int, input().split())
    heappush(que, (-p, d))

while que :
    p, d = heappop(que)
    for i in range(d, 0, -1) :
        if not visited[i] :
            visited[i] = True
            result -= p
            break

print(result)

### 빠른 알고리즘

# import sys, heapq
# input = sys.stdin.readline

# N = int(input())
# work = []
# for _ in range(N):
#     p, d = map(int, input().split())
#     heapq.heappush(work, (-d, -p))
# can, ans = [], 0
# if work:
#     maxday = -work[0][0]
#     for i in range(maxday, 0, -1):
#         while work and -i == work[0][0]:
#             heapq.heappush(can, heapq.heappop(work)[1])
#         if can:
#             ans -= heapq.heappop(can)
# print(ans)
