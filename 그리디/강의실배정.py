from heapq import heappush, heappop
import sys
input = sys.stdin.readline
N = int(input().rstrip())
que = []
rooms = [0]
for _ in range(N) :
    heappush(que, list(map(int, input().split())))
while que :
    s, e = heappop(que)
    x = heappop(rooms)
    if x > s :
        heappush(rooms, x)
    heappush(rooms, e)
print(len(rooms))

