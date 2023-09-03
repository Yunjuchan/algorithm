from heapq import heappush, heappop
N, M, K = map(int, input().split())
adj = [[] for _ in range(N+1)]
for _ in range(M) :
    s, e, w = map(int, input().split())
que = [[0,1]]