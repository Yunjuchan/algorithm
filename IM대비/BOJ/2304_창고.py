N = int(input())
lst = [0] * (1001)
L = []
for i in range(N) :
    i, n = map(int, input().split())
    lst[i] = n
    L.append([i,n])
    
L.sort()
Max = 0
Max_idx = []
for i in range(N) :
    if L[i][1] > Max :
        Max = L[i][1]
        Max_idx = [i]
    elif L[i] == Max :
        Max_idx.append(i)

## 올라가는 부분
for i in range(Max_idx[0]) :
    tmp = L[i][1]
    if tmp < L[i+1][1] :
        for j in range(L[i][0], L[i+1][0]) :
            lst[j] = L[i][1]
    else :
        for j in range(L[i][0], L[i+1][0]+1) :
            lst[j] = L[i][1]
        L[i+1][1] = L[i][1]

## 내려가는 부분
for i in range(N-1, Max_idx[-1], -1) :
    tmp = L[i][1]
    if tmp < L[i-1][1] :
        for j in range(L[i][0], L[i-1][0], -1) :
            lst[j] = L[i][1]
    else :
        for j in range(L[i][0], L[i-1][0]-1, -1) :
            lst[j] = L[i][1]
        L[i-1][1] = L[i][1]

## 최댓값들의 사이
for i in range(Max_idx[0], Max_idx[-1]) :
    lst[j] = Max
print(sum(lst))
