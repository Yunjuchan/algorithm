from heapq import heappush, heappop
import sys
input = sys.stdin.readline
def find(x) :
    if A[x] == 0 :
        return 0
    
    elif A[x] == x :
        A[x] -= 1
        return 1
    else :
        ret = find(A[x])
        return ret
    
N = int(input())
A = [i for i in range(1001)]
que = []
result = 0
for _ in range(N) :
    d, v = map(int, input().split())
    heappush(que, [-v, d])
while que :
    v, d = heappop(que)
    if find(d) == 1 :
        result -= v
print(result)
