# boj 11055

N = int(input())
arr = list(map(int, input().split()))
D = [0]*N
for i in range(N) :
    D[i] = arr[i]
for i in range(N) :
    for j in range(i) :
        if arr[i] > arr[j] :
            D[i] = max(D[i], D[j]+arr[i])
print(max(D))