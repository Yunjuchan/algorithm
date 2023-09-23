# boj 11053

N = int(input())
arr = list(map(int, input().split()))
C = [1] * N
for i in range(N) :
    for j in range(i) :
        if arr[j] < arr[i] :
            C[i] = max(C[i], C[j]+1)
print(max(C))