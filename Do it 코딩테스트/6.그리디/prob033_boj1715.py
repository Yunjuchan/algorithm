from heapq import heappop, heappush
import sys
input = sys.stdin.readline
N = int(input())
cnt = 0
cards = []
for i in range(N) :
    heappush(cards, int(input()))
if len(cards) == 1 :
    pass
else :
    while True :
        x = heappop(cards)
        y = heappop(cards)
        cnt += x + y
        if not cards:
            break
        heappush(cards, x+y)
print(cnt)

### heapq와 priorityQueue의 차이를 알아볼 수 있었음