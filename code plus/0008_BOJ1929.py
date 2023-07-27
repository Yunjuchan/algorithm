M, N = map(int, input().split())

Prime = [1] * (N+1)
Prime[0] = Prime[1] = 0
# print(M,N)
for i in range(2, N+1) :
    for j in range(2, N // i + 1) :
        Prime[i*j] = 0

for i in range(M, N+1) :
    if Prime[i] == 1 :
        print(i)

# 시간복잡도 O(nlogn으로 푼 풀이)
# 에라토스테네스의 체
