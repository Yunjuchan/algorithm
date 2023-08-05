import sys
input = sys.stdin.readline
N = int(input())
K = int(input())
prime = [True] * (N+1)
prime[0] = prime[1] = False
cnt = 0
soinsu = [1]
for i in range(2, int(N ** (1/2)) + 1) :
    for j in range(i, (N // i) + 1) :
        prime[i*j] = False

for i in range(1, N+1) :
    for p, bl in enumerate(prime[:]) :
        if bl and i % p == 0 :
             soinsu.append(p)
    if soinsu[-1] <= K :
        cnt += 1
print(cnt)




