import sys
input = sys.stdin.readline
pool = []
N, L = map(int, input().split())
now = 0
cnt = 0
for _ in range(N) :
    pool.append(list(map(int, input().split())))
pool.sort()
for s, e in pool :
    if now > s :
        tmp = (e - now + L-1) // L
        cnt += tmp
        now += L * tmp
    else :
        tmp = (e - s + L-1) // L
        cnt += tmp
        now = L * tmp + s
print(cnt)

