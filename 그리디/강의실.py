from heapq import heappush, heappop
import sys
input = sys.stdin.readline
N = int(input())
course = []
for _ in range(N) :
    n, s, e = map(int, input().split())
    heappush(course, [s,e,n])
room = [21e8]
while course :
    s, e, n = heappop(course)
    x = heappop(room) 
    if x > s :
        heappush(room, x)
    heappush(room, e)
print(len(room)-1)