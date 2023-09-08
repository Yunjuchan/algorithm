import sys
input = sys.stdin.readline
N, K = map(int, input().split())
lst = []
for _ in range(N) :
    M, V = map(int, input().split())
    lst.append([M, V])
lst.sort(key=lambda x :(-x[1], -x[0]))
bag = []
for _ in range(K) :
    bag.append(int(input()))
bag.sort(reverse=True)
i = j = 0
total = 0
while True :
    if i >= N or j >= K :
        break
    if lst[i][0] <= bag[j] :
        total += lst[i][1]
        j += 1
        i += 1
    elif lst[i][0] > bag[j] :
        i += 1
print(total)