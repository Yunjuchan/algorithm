# boj 11054

N = int(input())
arr = list(map(int, input().split()))
C1 = [1] * N
for i in range(N) :
    for j in range(i) :
        if arr[j] < arr[i] :
            C1[i] = max(C1[i], C1[j]+1)

C2 = [1] * N
for i in range(N-1, -1, -1) :
    for j in range(N-1, i, -1) :
        if arr[j] < arr[i] :
            C2[i] = max(C2[i], C2[j]+1)

Max = 0
for i in range(N) :
    if Max < C1[i]+C2[i] :
        Max = C1[i]+C2[i]
print(Max-1)
