import sys
input = sys.stdin.readline

Prime = [1] * (1000001)
Prime[0] = Prime[1] = 0
# print(M,N)
for i in range(3, 1000000 + 1, 2) :
    if Prime[i] == 0 :
        continue
    for j in range(3, int(1000000 // i) + 1, 2) :
        Prime[i*j] = 0
while True :
    N = int(input())
    if N == 0 :
        break
    for i in range(3, int(N // 2) + 1, 2) :
        if Prime[i] == 1 and Prime[N-i] == 1 :
            print(f'{N} = {i} + {N-i}')
            break
