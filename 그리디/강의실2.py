from heapq import heappush, heappop
import sys
input = sys.stdin.readline
N = int(input())
course = []
A = [0] * (N+1)
for _ in range(N) :
    n, s, e = map(int, input().split())
    heappush(course, [s,e,n])
s, e, n = heappop(course)
room = [[e, 1]]
A[n] = 1
cnt = 1
while course :
    s, e, n = heappop(course)
    x = heappop(room) 
    if x[0] > s :
        cnt += 1
        heappush(room, x)
        heappush(room, [e, cnt])
        A[n] = cnt
    else :
        heappush(room, [e, x[1]])
        A[n] = x[1]
print(cnt)
for i in range(1, N+1) :
    print(A[i])