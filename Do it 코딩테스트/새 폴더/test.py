import sys
input = sys.stdin.readline
N = int(input())
K = int(input())
prime = [True] * (N+1)
prime[0] = prime[1] = False
sejun = [1] * (N+1)
sejun[0] = 0
for i in range(2, int(N ** (1/2)) + 1) :
    for j in range(i, (N // i) + 1) :
        prime[i*j] = False

for i in range(2, N+1) :
    if prime[i] and i > K :
        for j in range(1, N // i + 1) :
            sejun[i*j] = 0
cnt = 0
for i in range(N+1) :
    cnt += sejun[i]
print(cnt)




