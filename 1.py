N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort(reverse=True)

lst2 = [0] * N
for i in range(N-1) :
    lst2[i] = lst[i] - lst[i+1]
for i in range(N-1, 0, -1) :
    lst2[i-1] += lst2[i]
height = 0
total = 0
for i in range(N-1) :
    total += (lst2[i] - lst2[i+1]) * (i+1)
    if total >= M :
        break
if total == M :
    height = lst[i+1]
elif total > M :
    x = (total-M) // (i+1)
    height = lst[i+1] + x
else :
    x = (M - total + N - 1) // N
    height = lst[-1] - x
print(height)
